import os
import openai
from dotenv import load_dotenv

OPEN_AI_CMDS = {
    'create_outline' : 'Create an outline for an essay about',
    'create_section' : 'Expand the blog section in to a detailed',
    'blog_ideas'     : 'Give me blog topic ideas on'
}

# davinci is the most accurate engine so default to this for now
OPEN_AI_ENGINE = 'text-davinci-002'

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def openai_blog_ideas(keyword, max_count=256):
    full_cmd = '%s %s:'%(OPEN_AI_CMDS['blog_ideas'], keyword)

    res = openai.Completion.create(
        engine=OPEN_AI_ENGINE,
        prompt=full_cmd,
        temperature=0.7,
        max_tokens=max_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return openai_get_completion_result(res)


def openai_create_outline(topic, max_count=150):
    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_outline'], topic)

    res = openai.Completion.create(
        engine=OPEN_AI_ENGINE,
        prompt=full_cmd,
        temperature=0,
        max_tokens=max_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return openai_get_completion_result(res)

def openai_create_section(section, max_count=256):
    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_section'], section)

    res = openai.Completion.create(
        engine=OPEN_AI_ENGINE,
        prompt=full_cmd,
        temperature=0.7,
        max_tokens=max_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return openai_get_completion_result(res)

def openai_get_completion_result(openai_res):
    return openai_res['choices'][0]['text']