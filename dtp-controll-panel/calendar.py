import calendar
from PIL import Image, ImageDraw, ImageFont

def create_calendar_image(year, month):
    # Create a calendar string
    cal = calendar.TextCalendar()
    cal_str = cal.formatmonth(year, month)

    # Set up image size and background
    img_width = 400
    img_height = 300
    background_color = (255, 255, 255)
    
    # Create a blank image
    img = Image.new('RGB', (img_width, img_height), background_color)
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Draw the calendar string on the image
    text_color = (0, 0, 0)
    draw.text((10, 10), cal_str, fill=text_color, font=font)

    # Save the image
    img.save(f'calendar_{year}_{month}.png')

# Specify year and month
year = 2024
month = 11

# Create the calendar image
create_calendar_image(year, month)
