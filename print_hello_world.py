from array import array
import string
check = False
import time
# Generate lowercase alphabets from a to z
alphabets_a_to_z = array('u', string.ascii_lowercase)

# Print each alphabet in the array
for alphabet in alphabets_a_to_z:
    word = alphabet
    loop = word
    if check:
        break
    print(loop)
    time.sleep(0.1)
    if word == 'h':
        for alphabet in alphabets_a_to_z:
            word = alphabet
            loop = 'h' + word
            if check:
                break
            print(loop)
            time.sleep(0.1)
            if loop == 'he':
                for alphabet in alphabets_a_to_z:
                    word = alphabet
                    loop = 'he' + word
                    if check:
                        break
                    print(loop)
                    time.sleep(0.1)
                    if loop == 'hel':
                        for alphabet in alphabets_a_to_z:
                            word = alphabet
                            loop = 'hel' + word
                            if check:
                                break
                            print(loop)
                            time.sleep(0.1)
                            if loop == 'hell':
                                for alphabet in alphabets_a_to_z:
                                    word = alphabet
                                    loop = 'hell' + word
                                    if check:
                                        break
                                    print(loop)
                                    time.sleep(0.1)
                                    if loop == 'hello':
                                        loop = 'hello' + " "
                                        if check:
                                            break
                                        print(loop)
                                        time.sleep(0.1)
                                        if loop == 'hello ':
                                            for alphabet in alphabets_a_to_z:
                                                word = alphabet
                                                loop = 'hello ' + word
                                                if check:
                                                    break
                                                print(loop)
                                                time.sleep(0.1)
                                                if loop == 'hello w':
                                                    for alphabet in alphabets_a_to_z:
                                                        word = alphabet
                                                        loop = 'hello w' + word
                                                        if check:
                                                            break
                                                        print(loop)
                                                        time.sleep(0.1)
                                                        if loop == 'hello wo':
                                                            for alphabet in alphabets_a_to_z:
                                                                word = alphabet
                                                                loop = 'hello wo' + word
                                                                if check:
                                                                     break
                                                                print(loop)
                                                                time.sleep(0.1)
                                                                if loop == 'hello wor':
                                                                    for alphabet in alphabets_a_to_z:
                                                                        word = alphabet
                                                                        loop = 'hello wor' + word
                                                                        if check:
                                                                             break
                                                                        print(loop)
                                                                        time.sleep(0.1)
                                                                        if loop == 'hello worl':
                                                                            for alphabet in alphabets_a_to_z:
                                                                                word = alphabet
                                                                                loop = 'hello worl' + word
                                                                                print(loop)
                                                                                time.sleep(0.1)
                                                                                if loop == 'hello world':
                                                                                    check = True
                                                                                    break
                                                                                
