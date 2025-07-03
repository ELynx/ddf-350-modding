# Set background color of all calls to RGB888_to_RGB565 according to the arguments used
# @author ELynx and o4-mini-high
# @category Visualization
# @description Highlight RGB888_to_RGB565 calls with the actual color loaded

from java.awt import Color

# locate the converter function symbol
prefix = "RGB888_to_RGB565"
sym_table = currentProgram.getSymbolTable()
symbols = []
for sym in sym_table.getAllSymbols(True):
    if sym.getName().startswith(prefix):
        symbols.append(sym)

if not symbols:
    println("Function symbol '%s*' not found. Check mangling or case." % prefix)
else:
    addrs = [sym.getAddress() for sym in symbols]
    for sym, addr in zip(symbols, addrs):
        println("Found %s at %s" % (sym.getName(), addr))

    # find all call-sites to that function
    refsTo = []
    for addr in addrs:
        refsTo.extend(list(currentProgram.getReferenceManager().getReferencesTo(addr)))

    if not refsTo:
        println("No calls/references to %s* found." % prefix)
    else:
        listing = currentProgram.getListing()

        for ref in refsTo:
            fromAddr = ref.getFromAddress()
            instr = listing.getInstructionAt(fromAddr)
            if instr is None:
                println(" Reference at %s is not an instruction, skipping." % fromAddr)
                continue

            # collect a window of prior instructions (up to 6 to resolve moves)
            prev_insns = []
            cur = instr
            for i in range(6):
                cur = cur.getPrevious()
                if cur is None:
                    break
                prev_insns.append(cur)

            # build mapping for registers r0, r1, r2 (including param_N)
            vals = {"r0": None, "r1": None, "r2": None}
            norm_map = {"param_1": "r0", "param_2": "r1", "param_3": "r2"}
            for insn in reversed(prev_insns):
                # normalize destination register
                op0_text = insn.getDefaultOperandRepresentation(0).lower().rstrip(",")
                dst = norm_map.get(op0_text, op0_text)
                if dst not in vals:
                    continue
                # try scalar immediate
                try:
                    scalar = insn.getScalar(0)
                    if scalar is not None:
                        vals[dst] = scalar.getValue()
                        continue
                except:
                    pass
                # get operand1 text
                op1_text = insn.getDefaultOperandRepresentation(1).lower().rstrip(",")
                # literal immediate
                if op1_text.startswith("#"):
                    try:
                        vals[dst] = int(op1_text.lstrip("#"), 16)
                        continue
                    except:
                        pass
                # register-to-register copy
                src = norm_map.get(op1_text, op1_text)
                if src in vals and vals[src] is not None:
                    vals[dst] = vals[src]
                    continue

            # ensure all RGB loaded
            if None in (vals["r0"], vals["r1"], vals["r2"]):
                println(" Missing color values before %s : %s" % (fromAddr, vals))
                continue

            # assign and clamp
            r = max(0, min(255, vals["r0"]))
            g = max(0, min(255, vals["r1"]))
            b = max(0, min(255, vals["r2"]))
            color = Color(r, g, b)

            # apply background highlight
            setBackgroundColor(fromAddr, color)
            println(" Highlighted %s with color #%02X%02X%02X" % (fromAddr, r, g, b))
