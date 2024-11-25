from llm_utils import llm
from filter_post import FilterPosts

filter= FilterPosts()


def get_length_str(length):
    """ Map the length categories to specific text"""

    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(tag, length, language):
    """Generate a linkedin post based on the preference"""

    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    """ Prepare the LLM prompt for post generation """
    
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    Please provide factual information with being a little creative and add some emoji characters,
    wherever it is necessary.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    filtered_examples = filter.get_filtered_posts(length, language, tag)

    if len(filtered_examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

        for i, post in enumerate(filtered_examples):
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'

            if i == 1: # Use max two samples
                break

    return prompt


if __name__ == "__main__":
    print(generate_post("Job Search", "Short", "English"))