



# Anticaptcha
  
Módulo para resolver captchas com anti-captcha  

*Read this in other languages: [English](Manual_Anticaptcha.md), [Português](Manual_Anticaptcha.pr.md), [Español](Manual_Anticaptcha.es.md)*
  
![banner](imgs/Banner_Anticaptcha.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Resolver ReCaptcha
  
Resolva ReCaptcha com a API https://anti-captcha.com
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Key Anticaptcha|Key da sua conta anticaptcha|Key|
|Url da página que contém ReCaptcha|Url da página para a qual o ReCaptcha será resolvido|Url da página|
|Token ReCaptcha|Token ReCaptcha que é obtido na página que contém ReCaptcha|Token|
|Variável onde o resultado será salvo|Variável onde o resultado será salvo|Variable|

### Resolver Captcha Imagen
  
Resolva um Captcha do tipo imagem com API do https://anti-captcha.com
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Key Anticaptcha|Key da sua conta Anticaptcha|Key|
|Rota da imagem|Rota para a imagem a ser resolvida|C:/Users/User/Desktop/captcha.png|
|Variável onde o resultado será salvo|Variável onde o resultado será salvo|Variável|

### Resolver hCaptcha
  
Resolva um Captcha do tipo hCaptcha com API de https://anti-captcha.com
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Key Anticaptcha|Key da sua conta Anticaptcha|Key|
|Token HCaptcha|Token HCaptcha que é obtido na página que contém HCaptcha|Token|
|URL da página com hCaptcha|URL da página onde o hCaptcha está localizado|URL|
|rqdata|Opcional. Dado extra que alguns sites usam para validar hCaptcha. Só preencha se a página mostrar 'rqdata'.|rqdata|
|Variável onde o resultado será salvo|Variável onde o resultado será salvo|Variável|
