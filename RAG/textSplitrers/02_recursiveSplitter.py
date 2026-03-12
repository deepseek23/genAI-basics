from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Whispering Leaves

In the heart of a forest, where sunlight weaves,
Gently sway the branches, whispering leaves.
A dance of soft shadows on the cool, damp ground,
Nature's sweet secret, in silence profound.

Through the tapestry of ages, stories unfold,
Of lovers and dreamers, of courage, of gold.
The murmurs of rivers, the songs of the breeze,
Caress the brave mountains, and tease the tall trees.

With a symphony vibrant, the wildflowers bloom,
Their colors, like laughter, dispel every gloom.
Underneath the vast sky, painted azure and white,
The stars share their wisdom, guiding through night.

Time flows like the river, forever it roams,
In the cradle of nature, we find ourselves home.
So sit in this stillness, let your worries cease,
And listen, dear heart, to the forest's whisper of peace."""
spliter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=15
)

result = spliter.split_text(text)

print(len(result))
print(result)