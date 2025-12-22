



# Anticaptcha
  
Module to resolve captcha with anti-captcha  

*Read this in other languages: [English](Manual_Anticaptcha.md), [Português](Manual_Anticaptcha.pr.md), [Español](Manual_Anticaptcha.es.md)*
  
![banner](imgs/Banner_Anticaptcha.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Resolve ReCaptcha
  
Resolve ReCaptcha with an API of https://anti-captcha.com
|Parameters|Description|example|
| --- | --- | --- |
|Key Anticaptcha|Key of your anticaptcha account|Key|
|Url of the page that has ReCaptcha|Url of the page to which the ReCaptcha will be resolved|Url|
|Token ReCaptcha|ReCaptcha Token that is obtained in the page that has ReCaptcha|Token|
|Variable where the Anticaptcha result is stored|Variable where the Anticaptcha result is stored|Variable|

### Resolve Image Captcha 
  
Resolve a Image Captcha with an API of https://anti-captcha.com
|Parameters|Description|example|
| --- | --- | --- |
|Key Anticaptcha|Key of your anticaptcha account|Key|
|Image path|Path to the image to be resolved|C:/Users/User/Desktop/captcha.png|
|Variable where the Anticaptcha result is stored|Variable where the result is stored|Variable|

### Resolve hCaptcha 
  
Resolve a hCaptcha type Captcha with https://anti-captcha.com API
|Parameters|Description|example|
| --- | --- | --- |
|Key Anticaptcha|Key of your anticaptcha account|Key|
|Token HCaptcha|HCaptcha Token that is obtained in the page that has HCaptcha|Token|
|URL of the page with hCaptcha|URL of the page where the hCaptcha is located|URL|
|rqdata|Optional. Extra data that some sites use to validate hCaptcha. Only fill it in if the page shows 'rqdata'.|rqdata|
|Variable where the Anticaptcha result is stored|Variable where the result is stored|Variable|
