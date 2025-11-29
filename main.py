def main():
    import sys

    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    try:
        total_cases = int(lines[0].strip())
    except ValueError:
        return

    def to_int_list(tokens, idx=0, acc=None):
        if acc is None:
            acc = []
        if idx == len(tokens):
            return acc
        acc.append(int(tokens[idx]))
        return to_int_list(tokens, idx + 1, acc)

    def sum_fourth_powers(nums, idx=0, acc=0):
        if idx == len(nums):
            return acc
        y = nums[idx]
        if y <= 0:
            acc += y * y * y * y
        return sum_fourth_powers(nums, idx + 1, acc)

    def process_case(case_idx, line_idx, outputs):
        if case_idx == total_cases or line_idx >= len(lines):
            return outputs

        x_line = lines[line_idx].strip() if line_idx < len(lines) else ""
        y_line = lines[line_idx + 1].strip() if line_idx + 1 < len(lines) else ""

        try:
            X = int(x_line)
        except ValueError:
            X = 0

        tokens = y_line.split() if y_line else []

        if len(tokens) != X:
            value = -1
        else:
            ys = to_int_list(tokens)
            value = sum_fourth_powers(ys)

        outputs.append(str(value))
        return process_case(case_idx + 1, line_idx + 2, outputs)

    results = process_case(0, 1, [])
    sys.stdout.write("
".join(results))


if __name__ == "__main__":
    main()
