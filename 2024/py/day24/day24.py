import sys
import pprint

example = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

with open('2024/py/day24/day24.txt') as f:
    s = f.read().strip()

data = example
data = s

a, b = data.split("\n\n")

signals = dict()
gates = []

for l in a.split('\n'):
    name, value = l.split(': ')
    value = int(value)
    signals[name] = value

opts = set()

for l in b.split('\n'):
    in1, opt, in2, _, name = l.split(' ')
    opts.add(opt)
    gates.append((name, in1, in2, opt))

# print(opts)

count = 0
while count < len(gates):
    # print(f"{count} | {len(gates)}")
    for g in gates:
        name, in1, in2, opt = g
        if name in signals:
            continue
        if in1 in signals and in2 in signals:
            if opt == 'XOR':
                signals[name] = signals[in1] ^ signals[in2]
            elif opt == 'AND':
                signals[name] = signals[in1] & signals[in2]
            elif opt == 'OR':
                signals[name] = signals[in1] | signals[in2]
            count += 1

signals = dict(sorted(signals.items()))

bstring = ''
for k, v in signals.items():
    # print(f"{k}: {v}")
    if k.startswith('z'):
        bstring += str(v)

bstring = ''.join(list(reversed(bstring)))

# print(bstring)
ans1 = int(bstring, 2)

print(ans1)
