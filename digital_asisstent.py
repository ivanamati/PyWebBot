import wolframalpha
import wikipedia



client = wolframalpha.Client("ATVE7L-94QT4PX37R")



def get_the_answer(upit):
    try:
        #wikipedia.set_lang(odabrani_jezik)
        wiki_rezultat = wikipedia.summary(upit, sentences=2)
        return wiki_rezultat
        #print(wiki_rezultat)

    except wikipedia.exceptions.DisambiguationError:

        results = client.query(upit).results
        wolfram_res = ""
        while True:
            try:
                result = next(results)
            except StopIteration:
                return "I'm sorry. There was no answer I could provide. \nGo back and try again."
                break
            wolfram_res = result.text
            #print(wolfram_res)
            return wolfram_res


    except wikipedia.exceptions.PageError:

        results = client.query(upit).results
        wolfram_res = ""
        while True:
            try:
                result = next(results)
            except StopIteration:
                return "I'm sorry. I couldn't find the answer. \nGo back and try again."
                break
            wolfram_res = result.text
            #print(wolfram_res)
            return wolfram_res
        
    except StopIteration:
        # Handle StopIteration exception and return a custom error message
        return "I'm sorry. I couldn't find the answer."

    except Exception as e:
        return f"I'm sorry.\nI found error {e} and I couldn't find the answer.\nPlease, go back and try again."
    

       

#get_the_answer("modric")