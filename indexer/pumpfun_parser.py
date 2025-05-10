PUMPFUN_PROGRAMS = [
    "PUMP111111111111111111111111111111111111111"  # replace with real contract IDs
]

def is_pumpfun_tx(tx):
    try:
        instructions = tx['transaction']['message']['instructions']
        return any(instr.get("programId") in PUMPFUN_PROGRAMS for instr in instructions)
    except KeyError:
        return False
