import dearpygui.dearpygui as dpg
import lang

INPUT_TEXT_WIDTH = 400

Obj =lang.Operate()
# 初期化
dpg.create_context()

# callback ラテン処理
def converse_callback_latin(sender, app_data, user_data):
    finally_text = Obj.latin(dpg.get_value('latin_sentence'), True)
    dpg.set_value(user_data, f'>>Result: {finally_text}')
    
# callback キリル処理
def converse_callback_cyrillic(sender, app_data, user_data):
    str1 = dpg.get_value("cyrillic_sentence")
    str_1 = str1.encode('windows-1252')
    str_2 = str_1.decode("cp1251")
    finally_text = Obj.cyrillic(str_2, False)
    dpg.set_value(user_data, f'>>Result: {finally_text}')

# フォント設定
with dpg.font_registry():
    with dpg.font(file="./fonts/Roboto-Medium.ttf", size=25) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    dpg.bind_font(default_font)
    # with dpg.font(file="./fonts/Roboto-Bold.ttf", size=20) as small_font:
    #     dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

# メインウィンドウ設定
with dpg.window(label='main_window', tag='main_window'):
    # LATIN
    dpg.add_text('>>Input LATIN sentence')
    dpg.add_input_text(label='Latin', tag='latin_sentence', width=INPUT_TEXT_WIDTH)
    dpg.add_button(label='Converse', tag='latin_button', callback=converse_callback_latin, user_data='result_text')

    dpg.add_separator()

    # CYRILLIC
    dpg.add_text('>>Input CYRILLIC sentence')
    dpg.add_input_text(label='Cyrillic', tag='cyrillic_sentence', width=INPUT_TEXT_WIDTH)
    dpg.add_button(label='Converse', tag='cyrillic_button', callback=converse_callback_cyrillic, user_data='result_text')

    dpg.add_separator()
    dpg.add_text(tag='result_text')

# 後処理
dpg.create_viewport(title="dear_pygui", width=510, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('main_window', True)
dpg.start_dearpygui()
dpg.destroy_context()
