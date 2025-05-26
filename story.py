import random

characters = ["a brave knight", "a clever princess", "a mischievous dragon", "an adventurous robot"]
settings = ["in a haunted castle", "on a distant planet", "in a magical forest", "at the edge of a volcano"]
problems = ["found a mysterious map", "lost their way", "discovered a hidden treasure", "had to save the kingdom"]
resolutions = ["by solving tricky riddles", "with the help of new friends", "after a daring escape", "using their special powers"]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    problem = random.choice(problems)
    resolution = random.choice(resolutions)

    story = f"Once upon a time, {character} {setting} {problem}. They overcame the challenge {resolution}."
    return story

