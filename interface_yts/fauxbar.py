import time

def animation():
    barload = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

    i = 0

    while i < 20:
        print(barload[i % len(barload)], end='\r')
        time.sleep(.1)
        i += 1