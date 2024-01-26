"""
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it.
This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:
If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user
    enters the correct answer after the 8-second limit.
"""

import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    prompt = f'#{question_number}: {num1} x {num2} = '
    
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(
            prompt,
            allowRegexes=[f'^{num1 * num2}$'],
            blockRegexes=[('.*', 'Incorrect!')],
            timeout=8,
            limit=3
        )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correct_answers += 1
    time.sleep(1)  # Brief pause to let user see the result.
print(f'Score: {correct_answers} / {number_of_questions}')
