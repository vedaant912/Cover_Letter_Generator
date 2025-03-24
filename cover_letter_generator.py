from llm_helper import llm
import ast

def generate_cover_letter(role, company, hook, resume):

    prompt = f"You are writing a cover letter applying for the {role} role at {company}. Here's what you have so far: \n{hook}\nFinish writing the cover letter based on your resume and keep it within 250 words.Keep what we have so far, word for word.\nHere’s your resume: {resume}\n And Keep the format as follows:\nDear Hiring Manager,\nCONTENT THAT IS GENERATED\nSincere Regards,\n[Your_Name]\nMake sure the output doesnnot have any extra quotes around it. There should not be any preamble, just the content that is directly used as output. Make sure the hook the first paragraph shouldn't be made up data. Make sure everything aligns with job description and resume."

    cover_letter = llm.invoke(prompt)
    return cover_letter.content

def generate_hook(challenges, role, company):

    prompt = f"You are applying for this {role} position at {company}. Write an attention-grabbing hook for your cover letter that highlights your experience and qualifications in a way that shows you empathize and can successfully take on the challenges of the {role} role. Consider incorporating specific examples of how you have tackled these challenges in your past work, and explore creative ways to express your enthusiasm for the opportunity. Keep your hook within 100 words. Donot make up additional data regarding my experiences and educational background.\n Challenges = {challenges}"

    hook = llm.invoke(prompt)
    return hook.content

def fetch_biggest_challenge(job_description):

    prompt =  f"Based on this job description, what is the biggest challenge someone in this position would face day-to-day? Give me the root cause of this issue.\n{job_description}"

    challenges = llm.invoke(prompt)
    return challenges.content

def get_attributes(job_description):

    prompt = f"On the basis of the following job description return the role and company in following format for python list : [role, company_name]. Only one item for role and company name.\nJob Description:{job_description}"

    attributes = llm.invoke(prompt)
    return ast.literal_eval(attributes.content)


def get_cover_letter(resume, job_description):

    # company = "SAP"
    role, company = get_attributes(job_description)

    # Get biggest challenge
    challenges = fetch_biggest_challenge(job_description)

    # Create a attention-grabbing-hook (input: role, background)
    hook = generate_hook(challenges, role, company)

    # Generate final cover letter using initial hook
    cover_letter = generate_cover_letter(role, company, hook, resume)

    return cover_letter




