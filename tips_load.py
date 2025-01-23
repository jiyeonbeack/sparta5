import seaborn as sns

def get_tips():
    tips = sns.load_dataset("tips")
    return tips

def print_get():
    return "일어나세요 용사여"

if __name__ == "__main__":
    print_get()