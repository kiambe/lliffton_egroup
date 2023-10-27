from appuser.Utils.levels.level0 import *
from appuser.Utils.levels.level1 import *
from appuser.Utils.levels.level2 import *
from appuser.Utils.levels.level3 import *
from appuser.Utils.levels.level4 import *
from appuser.Utils.levels.level5 import *
from appuser.Utils.levels.level6 import *



def response_main_with_text(text, custom_text, 
    phone_number, custom_text_two,member_id
    ):
    level = len(custom_text)
    if level == 0:
        print("is in level 0")
        return level0(custom_text)
        return response_menu_landing(custom_text_two)

    if level == 1:
        print("is in level 1")
        return level1(custom_text,member_id)
    
    if level == 2:
        print("is in level 1")
        return level2(custom_text)
    if level == 3:
        print("is in level 3")
        return level3(custom_text,member_id)
    if level == 4:
        print("is in level 1")
        return level4(custom_text,member_id)
    if level == 5:
        print("is in level 5")
        return level5(custom_text)
    if level == 6:
        print("is in level 6")
        return level6(custom_text,member_id)