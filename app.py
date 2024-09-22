import streamlit as st
from datetime import datetime

# Function to determine astrological sign based on date of birth
def get_astrological_sign(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn.", "images/capricorn.jpg", "You are disciplined, responsible, and ambitious. You are a natural achiever who\
                works hard to accomplish your goals. Practical and grounded, you value tradition and \
                    often take a methodical approach to life. Capricorns can sometimes be seen as serious \
                        or reserved, but their dedication and persistence make them incredibly reliable. \
                            You are a long-term planner who focuses on building a secure future."
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius.", "images/aquarius.jpg", "You are independent, innovative, and forward-thinking. You are a visionary who often challenges\
                the status quo and seeks to bring about positive change. Your humanitarian nature drives you to \
                    advocate for social justice and equality. Aquarians value individuality and freedom, often marching\
                        to the beat of their own drum. While they are intellectually driven, they can sometimes appear \
                            detached or aloof in emotional situations."
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces.", "images/pisces.jpg", "You are empathetic, dreamy, and intuitive. You are highly imaginative and often drawn to artistic \
                and creative pursuits. Your deep sensitivity allows you to connect with others on an emotional level,\
                    but it can also make you prone to escapism or becoming overwhelmed by your emotions. Pisceans are\
                        compassionate and often put others' needs before their own, seeking spiritual or emotional fulfillment \
                            in life."
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries.", "images/aries.jpg", "You are a pioneer, \
            driven by passion and enthusiasm. You love taking initiative and thriving in competitive environments.\
                Your impulsive nature makes you quick to act, often before fully thinking things through, \
                    but your courage and optimism keeps you moving forward. Aries individuals can be assertive and direct,\
                        sometimes seen as blunt, but they are always up for a challenge."
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus.", "images/taurus.jpg", "You are known for your love of comfort and stability.\
                You appreciate the finer things in life, from good food to beautiful surroundings. \
                    Reliable and patient, you work steadily toward your goals. \
                        However, your stubborn nature can sometimes make you resistant to change.\
                            Loyal and determined, once you commit to something, you stick with it through thick and thin."
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini.", "images/gemini.jpg", "You are versatile and quick-witted. You love to learn new things and to share your knowledge with others. \
                Your dual nature allows you to adapt to different situations easily, but it can also make you appear\
                    inconsistent or indecisive. Social and curious, you thrive on intellectual conversations\
                        and enjoy connecting with a variety of people."
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer.", "images/cancer.jpg", "You are deeply emotional and intuitive, often picking up on the feelings of others. \
                You are highly protective of your loved ones and you value close, nurturing relationships. \
                    Your sensitivity can make you vulnerable, but it also gives you a unique ability \
                        to connect with others on a deep level. You are a homebody at heart and often seek security \
                            in familiar environments."
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo.", "images/leo.jpg", "You are a natural-born leader with a flair for the dramatic.\
                You are confident, charismatic, and you love being the center of attention.\
                    Generous and warm-hearted, you enjoy making others feel special, but you also crave admiration and\
                        respect in return. Leos have a strong sense of self and pride, and they are highly creative, \
                            often excelling in artistic or expressive pursuits."
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo.", "images/virgo.jpg", "You are meticulous, analytical, and highly practical. \
                You are detail-oriented and have a strong desire for order and efficiency. \
                    Often perfectionist, you can be critical of yourself and others,\
                        but this comes from a deep desire to improve and be of service.\
                            Virgos are highly dependable and hardworking, often excelling \
                                in tasks that require organization and attention to detail."
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra.", "images/libra.jpg", "You seek harmony, balance, and fairness in all areas of life. \
                You are diplomatic and skilled at seeing both sides of an issue, \
                    which makes you an excellent mediator. Social by nature, you thrive \
                        in relationships and value companionship. However, your desire to please \
                            others can make you indecisive, as you often struggle to make choices \
                                that might upset the equilibrium."
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio.", "images/scorpio.jpg", "You are known for your intensity and passion. \
                You feel things deeply and you are often drawn to the mysteries of life. \
                    Your emotional depth can make you magnetic and intriguing, but it \
                        can also lead you to be secretive or possessive. Scorpios are highly determined, \
                            and once they set their sights on something, they pursue it with relentless focus.\
                                You value loyalty and can be incredibly transformative in your relationships."
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius.", "images/sagittarius.jpg", "You are adventurous, optimistic, and you are always seeking the bigger picture.\
                You are a free spirit who loves exploring new ideas, cultures, and philosophies. \
                    Your blunt honesty can sometimes come off as tactless, but your intentions \
                        are usually driven by a desire for truth. Sagittarians are philosophical and \
                            idealistic, and they are constantly in search of meaning and wisdom in life."
    else:
        return "Unknown", None, ""

# Streamlit app structure
def main():
    st.title("Astrological Sign Calculator")
    
    name = st.text_input("What's your name?")
    birth_date = st.date_input("Enter your birth date")

    if st.button("Calculate My Sign"):
        sign, image_path, description = get_astrological_sign(birth_date.month, birth_date.day)
        st.write(f"Hello, {name}! You were born on {birth_date}.")
        st.write(f"Your astrological sign is {sign}.")
        st.write(description)
    
        if image_path:
            st.image(image_path, caption=f"Your sign is {sign}", use_column_width=True)

if __name__ == "__main__":
    main()
