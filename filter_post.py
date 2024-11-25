import pandas as pd
import json


class FilterPosts:
    def __init__(self, file_path="app_data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        """ load the processed posts from json file and get unique tags"""

        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            # collect unique tags
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        """ Filter the posts for a given tag, language and length variables"""

        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  # Tags contain 'Influencer'
            (self.df['language'] == language) &  # Language is 'English'
            (self.df['length'] == length)  # Line count is less than 5
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        """ Assign a length category based on the line count of a post"""
        
        if line_count < 3:
            return "Short"
        elif 3 <= line_count <= 9:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FilterPosts()
    # print(fs.get_tags())
    posts = fs.get_filtered_posts("Medium","English","Job Search")
    print(posts)