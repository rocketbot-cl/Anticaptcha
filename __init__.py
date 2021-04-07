# coding: utf-8

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Anticaptcha' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""
try:

    if module == "ReCaptchaV2":
        from anticaptchaofficial.recaptchav2proxyless import *

        site_key = GetParams("sitekey")
        api_key = GetParams("apikey")
        url = GetParams("url")
        var_ = GetParams("result")

        if not api_key:
            raise Exception("Api key field is empty")
        if not site_key:
            raise Exception("Site key field is empty")

        solver = recaptchaV2Proxyless()
        solver.set_verbose(1)
        solver.set_key(api_key)
        solver.set_website_url(url)
        solver.set_website_key(site_key)

        g_response = solver.solve_and_return_solution()
        if g_response != 0 and var_:
            SetVar(var_, g_response)
        else:
            print(solver.error_code)
            SetVar(var_, solver.error_code)


    """
        Resuelvo captcha tipo imagen
    """

    if module == "captchaimagen":
        from anticaptchaofficial.imagecaptcha import *

        api_key = GetParams("apikey")
        var_ = GetParams("result")
        path_ = GetParams("path")

        if not api_key:
            raise Exception("Api key field is empty")

        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key(api_key)

        captcha_text = solver.solve_and_return_solution(path_)
        if captcha_text != 0 and var_:
            SetVar(var_, captcha_text)
        else:
            print("task finished with error " + solver.error_code)
            SetVar(var_, solver.error_code)

except Exception as e:
    print("\x1B[" + "31;40m" + str(e) + "\x1B[" + "0m")
    PrintException()
    raise e
