import argparse
import struct
import csv

def assemble(input_file, binary_output, log_output):
    """Ассемблер: преобразует текстовый код в бинарный и логирует процесс в CSV."""
    commands = {
        "LOAD_CONST": 0x15,  # A=21, команда загрузки константы
        "LOAD_MEM": 0x0A,    # A=10, команда чтения из памяти
        "STORE_MEM": 0x00,   # A=0, команда записи в память
        "MUL": 0x12,         # A=18, команда умножения
    }

    binary_data = bytearray()
    log_entries = []

    with open(input_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            cmd = parts[0]
            if cmd not in commands:
                raise ValueError(f"Неизвестная команда: {cmd}")

            a = commands[cmd]
            b = int(parts[1]) if len(parts) > 1 else 0

            if cmd == "MUL":
                b = 0  # Для MUL значение B всегда 0

            # Формируем 4-байтную инструкцию
            instruction = (a & 0x1F) | ((b & 0x1FFFFF) << 5)
            instruction_bytes = struct.pack("<I", instruction)
            binary_data.extend(instruction_bytes)

            log_entries.append([cmd] + [f"{byte:#04X}" for byte in instruction_bytes])

    with open(binary_output, "wb") as f:
        f.write(binary_data)

    with open(log_output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Команда", "Байт1", "Байт2", "Байт3", "Байт4"])
        writer.writerows(log_entries)

    print(f"Ассемблирование завершено. Бинарный файл сохранён в {binary_output}, лог сохранён в {log_output}.")

def interpret(binary_file, memory_range, result_file):
    """Интерпретатор: выполняет бинарный код и сохраняет память в CSV."""
    with open(binary_file, "rb") as f:
        binary_data = f.read()

    memory = [0] * 2048  # Массив памяти размером 2048 ячеек
    stack = []
    pc = 0  # Счётчик команд

    while pc < len(binary_data):
        instruction = struct.unpack("<I", binary_data[pc:pc + 4])[0]
        pc += 4

        a = instruction & 0x1F
        b = (instruction >> 5) & 0x1FFFFF

        # Отладочный вывод: текущее состояние интерпретатора
        print(f"ПК={pc - 4:08X}: Инструкция={instruction:08X}, A={a}, B={b}")
        print(f"Стек до операции: {stack}")

        if a == 0x15:  # LOAD_CONST (A=21)
            stack.append(b)
            print(f"LOAD_CONST: Добавлено {b} в стек")
        elif a == 0x0A:  # LOAD_MEM (A=10)
            if 0 <= b < len(memory):
                stack.append(memory[b])
                print(f"LOAD_MEM: Добавлено значение memory[{b}] = {memory[b]} в стек")
            else:
                raise ValueError(f"Обращение к памяти вне допустимого диапазона: {b}")
        elif a == 0x00:  # STORE_MEM (A=0)
            if len(stack) < 2:
                print(f"Ошибка: В стеке всего {len(stack)} элементов, требуется 2 для STORE_MEM.")
                raise ValueError("Недостаточно элементов в стеке для выполнения STORE_MEM.")
            addr = stack.pop()
            value = stack.pop()
            if 0 <= addr < len(memory):
                memory[addr] = value
                print(f"STORE_MEM: Сохранено значение {value} в memory[{addr}]")
            else:
                raise ValueError(f"Обращение к памяти вне допустимого диапазона: {addr}")
        elif a == 0x12:  # MUL (A=18)
            if len(stack) < 2:
                print(f"Ошибка: В стеке всего {len(stack)} элементов, требуется 2 для MUL.")
                raise ValueError("Недостаточно элементов в стеке для выполнения MUL.")
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 * op2
            stack.append(result)
            print(f"MUL: {op1} * {op2} = {result}")
        else:
            raise ValueError(f"Неизвестная инструкция: A={a}, B={b}")

        print(f"Стек после операции: {stack}\n")

    # Записываем память в CSV
    start, end = memory_range
    with open(result_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Адрес", "Значение"])
        for i in range(start, end):
            writer.writerow([i, memory[i]])

    print(f"Интерпретация завершена. Память сохранена в {result_file}.")

def main():
    parser = argparse.ArgumentParser(description="Учебная виртуальная машина (УВМ)")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Режим работы")

    # Ассемблер
    asm_parser = subparsers.add_parser("assemble", help="Ассемблировать текстовую программу")
    asm_parser.add_argument("input_file", type=str, help="Файл с текстовой программой")
    asm_parser.add_argument("binary_output", type=str, help="Файл для сохранения бинарного кода")
    asm_parser.add_argument("log_output", type=str, help="Файл для сохранения CSV-лога")

    # Интерпретатор
    int_parser = subparsers.add_parser("interpret", help="Интерпретировать бинарный код")
    int_parser.add_argument("binary_file", type=str, help="Бинарный файл с кодом")
    int_parser.add_argument("start", type=int, help="Начальный адрес диапазона памяти")
    int_parser.add_argument("end", type=int, help="Конечный адрес диапазона памяти")
    int_parser.add_argument("result_file", type=str, help="Файл для сохранения результата")

    args = parser.parse_args()

    if args.mode == "assemble":
        assemble(args.input_file, args.binary_output, args.log_output)
    elif args.mode == "interpret":
        interpret(args.binary_file, (args.start, args.end), args.result_file)

if __name__ == "__main__":
    main()
