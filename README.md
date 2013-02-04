Description
------------------
Due to the limitation of embedded Python with Sublime Text 2, [ConvertToUTF8](https://github.com/seanliang/ConvertToUTF8) might not work properly.

To solve this problem, you can try:

(1) Install Codecs26 plugin. This plugin is compiled under 64bit Ubuntu, I'm not sure if it works with other Linux distro or 32-bit platforms.

(2) If the above method doesn't work, you will have to install Python 2.6 manually with these commands:
<code>  
sudo add-apt-repository ppa:fkrull/deadsnakes  
sudo apt-get update  
sudo apt-get install python2.6  
sudo ln -s /usr/lib/python2.6 /[PATH_TO_ST2]/lib  
</code>
** Note: PATH_TO_ST2 means the installation location of Sublime Text 2 **

I'm working on making ConvertToUTF8 support both Sublime Text 2 and 3 currently. If this plugin is useful for you, you might want to buy me a cup of coffee to keep me fresh. Thanks for everyone's help! :)

[![Buy me a cup of coffee via PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=GP6Y25N7Q9E26&lc=US&item_name=Buy%20me%20a%20cup%20of%20coffee&item_number=ConvertToUTF8&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHostedGuest)
[![Buy me a cup of coffee via Alipay](http://dl.dropbox.com/u/31937639/alipay.png)](https://me.alipay.com/seanliang)

Installation
------------------
Using [Package Control](http://wbond.net/sublime_packages/package_control) to find, install and upgrade *Codecs26* is the recommended method to install this plug-in.

Otherwise, you can download this repository as a zip file, unzip it, and rename the new folder to *Codecs26*, then move this folder to *Packages* folder of Sublime Text (You can find the *Packages* folder by clicking "Preferences > Browse Packages" menu entry in Sublime Text).

Contact me
------------------
Please send me your questions or suggestions: sunlxy (at) yahoo.com or http://weibo.com/seanliang
