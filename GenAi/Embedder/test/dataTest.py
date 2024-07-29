import json
# data = [text: "jghgj"]
# parsed_data = json.loads(data)
# print(parsed_data)

import re
data = "[{\n'Question': 'Describe the ambiance of the forest as dawn breaks?'\n'Answer': 'As dawn broke, the forest awoke from its slumber, stretching its limbs of leaves and branches toward the sky. Each dewdrop, a tiny jewel of nature, shimmered in the soft light, reflecting a thousand tiny rainbows. The tranquility of the scene was almost palpable, a serene prelude to the day\u2019s adventures in the wild.'\n},\n{\n'Question': 'How does the forest change as you walk deeper into it?'\n'Answer': 'As you walked deeper into the forest, the sounds of civilization faded, replaced by the symphony of the wild. The gentle rustling of leaves was accompanied by the distant call of a woodpecker, its rhythmic drumming a testament to the forest\u2019s dynamic ecosystem. The occasional chirp of a cricket added a layer of quiet harmony, while the soft murmur of a nearby brook provided a soothing undertone.'\n},\n{\n'Question': 'What types of flora and fauna are found in the clearing near the brook?'\n'Answer': 'In a small clearing near the brook, wildflowers bloomed in an explosion of colors. Their petals, vibrant shades of violet, yellow, and crimson, created a stark contrast against the lush green backdrop. Butterflies, with wings like delicate stained glass, danced from flower to flower, their presence a testament to the intricate web of life that thrived in this serene corner of the world.'\n},\n{\n'Question': 'How does the forest transform as midday approaches?'\n'Answer': 'As midday approached, the forest seemed to come alive with a new energy. The sun, now high in the sky, poured its light through the trees, casting long, angular shadows across the path. The heat was tempered by the cool shade of the forest, creating a perfect balance of warmth and respite. In this light, the forest seemed to shimmer with an almost magical quality, a testament to its ancient and enduring beauty.'\n},\n{\n'Question': 'Describe the transition from day to night in the forest?'\n'Answer': 'The transition from day to night was gradual, a slow and serene process that allowed the forest to prepare for the coming darkness. The sounds of the forest changed too, with the daytime chorus of birds giving way to the more subdued calls of nocturnal creatures. The evening brought with it a quiet stillness, broken only by the occasional rustle of leaves or the distant hoot of an owl.'\n}]"

# parsed_data = json.loads(data)


ddata = "{\n'Question': 'What does the morning sun do?',\n'Answer': 'The morning sun crests the horizon, casting a warm golden glow over the sprawling wilderness.'\n}\n{\n'Question': 'How does the path through the forest appear?',\n'Answer': 'The path through the forest is a ribbon of possibility, winding through ancient trees whose trunks were wrapped in intricate patterns of moss and ivy.'\n}\n{\n'Question': 'What is the sound of the forest like?',\n'Answer': 'The sounds of civilization fade away as you walk deeper into the forest, replaced by the symphony of the wild. The gentle rustling of leaves is accompanied by the distant call of a woodpecker, its rhythmic drumming a testament to the forest\u2019s dynamic ecosystem.'\n}\n{\n'Question': 'How does the forest change as midday approaches?',\n'Answer': 'As midday approaches, the forest seems to come alive with a new energy. The sun, now high in the sky, pours its light through the trees, casting long, angular shadows across the path. The heat is tempered by the cool shade of the forest, creating a perfect balance of warmth and respite.'\n}\n{\n'Question': 'What does the forest look like as the sun begins to set?',\n'Answer': 'As the sun begins its descent, the forest takes on a different character. The light softens, casting a warm, golden hue over everything. The shadows grow longer, and the air becomes cooler. The transition from day to night is gradual, a slow and serene process that allows the forest to prepare for the coming darkness.'\n}"


# Long string to be parsed
long_string = "[{\n'Question':'What did the sunlight do as it rose over the horizon?',\n'Answer':'The sunlight cast a warm golden glow over the sprawling wilderness.'\n},\n{\n'Question':'How did the trees appear in the forest?',\n'Answer':'The trees appeared ancient, with their trunks wrapped in intricate patterns of moss and ivy.'\n},\n{\n'Question':'What did the brook represent in the forest?',\n'Answer':'The brook represented a life-giving force that sustained the myriad forms of flora and fauna along its banks.'\n},\n{\n'Question':'What changes occurred in the forest as midday approached?',\n'Answer':'The forest came alive with new energy as the sun poured its light through the trees, casting long, angular shadows across the path.'\n},\n{\n'Question':'What was the effect of the darkness on the forest as night fell?',\n'Answer':'The darkness was not oppressive but rather a gentle embrace that allowed the forest to reveal its hidden secrets.'\n}]"
pattern = re.compile(
    r"'Question':\s*'([^']+?)'\s*,\s*'Answer':\s*'([^']+?)'", re.DOTALL)

# Find all matches in the long string
matches = pattern.findall(long_string)

# Initialize the list of dictionaries
qa_list = [{'Question': question, 'Answer': answer}
           for question, answer in matches]

# Print the list of dictionaries
print(qa_list)
