
基于Pandora 的 Serveless 个人免登录免翻墙 zbur部署（需要有chatgpt账户）

(一) 首先注册Zeabur 绑定github使用, clone 本项目到自己的仓库

(二) 用魔法登录chatgpt官网 https://chat.openai.com/ 后打开 https://chat.openai.com/api/auth/session 复制字典中token 的值待用

(三) 回到Zeabur 参考教程 https://zeabur.com/docs/zh-CN/get-started  将自己Github中clone来的本项目一键部署

(四) 参考 https://zeabur.com/docs/zh-CN/environment/variables  在 Zeabur 当前面板下面Variable 添加一个变量： Key 是 MYTOKEN ，Value 是前面复制来的token

(五) 参考 https://zeabur.com/docs/zh-CN/deploy/domain-binding 在 Zeabur 当前面板下面的 Domains 中设置一个域名，即可免翻墙打开该域名访问chatgpt
