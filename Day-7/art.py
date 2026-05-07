logo = """

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
"""

word_bank = [
    "python", "javascript", "java", "ruby", "swift", "kotlin", "typescript",
    "computer", "laptop", "keyboard", "monitor", "printer", "scanner", "router",
    "internet", "website", "browser", "server", "database", "network", "cloud",
    "developer", "programmer", "engineer", "designer", "analyst", "manager",
    "algorithm", "function", "variable", "dictionary", "list", "tuple", "string",
    "integer", "boolean", "float", "array", "object", "class", "method",
    "apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple",
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin", "octopus", "butterfly",
    "mountain", "ocean", "river", "forest", "desert", "valley", "canyon",
    "beautiful", "fantastic", "wonderful", "amazing", "brilliant", "excellent",
    "quickly", "silently", "happily", "sadly", "angrily", "patiently", "bravely"
]

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']