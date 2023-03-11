# pico espresso - a $35 wifi enabled universal espresso machine PID mod
*A simple Raspberry Pi Pico w based espresso machine controller with support for duty cycled PID with SSR and OLED*

Can be installed on any espresso machine for temperature control but currently installed on a Calphalon temp iq

USE AT YOUR OWN RISK

Future support for:
+ additional asynch updated and control via web page
+ zero crossing triac (robotdyn) pump control
+ flow meter (comes installed on temp iq)
+ load cell hx711

<img width="416" alt="image" src="https://user-images.githubusercontent.com/7244561/224496973-89da0e37-e7f7-4ca5-bb81-930c0f0aa255.png">

![image](https://user-images.githubusercontent.com/7244561/224459490-87351a9d-1f44-41a7-92be-3cdb52296e52.png)

BOM ($35 to $67 depending on basic (ssr + pico + max6675 + tap) to complete (Add oled, load cell and dimmer)
+ [OLED](https://www.amazon.com/gp/product/B072Q2X2LL/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1) $7
+ [SSR](https://www.amazon.com/gp/product/B08GPB7N2T/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) $11
+ [pico w](https://www.microcenter.com/product/650108/raspberry-pi-pico-w) $6
+ [max6675](https://www.amazon.com/gp/product/B01HT871SO/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) $7.69
+ [m6x1.0 tap and bit for thermocouple mounting on thermoblock using stock M4 hole location](https://www.amazon.com/uxcell-Spiral-Titanium-Machine-Threading/dp/B09TYS683J/ref=sr_1_4?keywords=m6+x+1+tap+and+bit&qid=1678515435&sr=8-4) $9
+ [hx711](https://www.amazon.com/gp/product/B08KRV8VYP/ref=ppx_yo_dt_b_asin_title_o07_s03?ie=UTF8&psc=1) $8
+ [robodyne zc triac dimmer](https://www.amazon.com/gp/product/B071X19VL1/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) $15
