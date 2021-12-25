from silky_mes_gui import SilkyMesGUI

debug = False


def test(mode: str):
    # diss, ass, diss_for_hack...
    from silky_mes import SilkyMesScript

    script_mes = "LIBLARY.LIB"
    file_txt = "LIBLARY.txt"

    if mode == "diss":
        new_script = SilkyMesScript(script_mes, file_txt, verbose=True, debug=False)
        new_script.disassemble()
        del new_script
    elif mode == "ass":
        new_script = SilkyMesScript(script_mes, file_txt, verbose=True, debug=False)
        new_script.assemble()
        del new_script
    elif mode == "diss_for_hack":
        new_script = SilkyMesScript(script_mes, file_txt, verbose=True, debug=True, hackerman_mode=True)
        new_script.disassemble()
        del new_script


def main():
    gui = SilkyMesGUI()
    return True


if __name__ == '__main__':
    if debug:
        test("diss")
    else:
        main()
