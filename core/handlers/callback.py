import sqlite3

from aiogram import Bot
from aiogram.types import CallbackQuery


async def select_object(call: CallbackQuery, bot: Bot):
    con = sqlite3.connect('./Lektorey.db')
    cur = con.cursor()
    if call.data == "foreign_language_in_the_field_of_jurisprudence_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 1''', ).fetchall()
    elif call.data == "elective_disciplines_in_physical_culture_and_sports_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 2''', ).fetchall()
    elif call.data == "criminal_law_callback":
        wrem = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 3''', ).fetchall()
    elif call.data == "labor_Law_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 4''', ).fetchall()
    elif call.data == "criminology_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 5''', ).fetchall()
    elif call.data == "sociocultural_communication_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 6''', ).fetchall()
    elif call.data == "family_law_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 7''', ).fetchall()
    elif call.data == "tax_law_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 8''', ).fetchall()
    elif call.data == "civil_law_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 9''', ).fetchall()
    elif call.data == "life_safety_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 10''', ).fetchall()
    elif call.data == "the_right_of_obligatory_security_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 11''', ).fetchall()
    elif call.data == "english_language_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 12''', ).fetchall()
    elif call.data == "german_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 13''', ).fetchall()
    elif call.data == "russian_history_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 14''', ).fetchall()
    elif call.data == "basics_of_programming_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 15''', ).fetchall()
    elif call.data == "mathematical_analysis_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 16''', ).fetchall()
    elif call.data == "physics_callback":
        wrem = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 17''', ).fetchall()
        print(wrem)
        for el in wrem:
            name, path = el
            await call.message.answer(f"Видеоуроки по теме: {name}")
            try:
                with open(path, "r", encoding="utf8") as txt:
                    sp = txt.readlines()
                    for url in sp:
                        print(name, url)
                        await call.message.answer(f'<a {url}</a>',
                                                  parse_mode="HTML",
                                                  disable_web_page_preview=True)
            except Exception as error:
                print("Файл не найден")
    elif call.data == "fundamentals_of_economics_and_financial_literacy_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 18''', ).fetchall()
    elif call.data == "discrete_mathematics_callback":
        answer = cur.execute(
            '''SELECT name_lecture, addres_lecture FROM Lectures WHERE id = 19''', ).fetchall()
    await call.message.edit_reply_markup()
