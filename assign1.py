class CreativePoster:
    def _init_(self, title, theme, designer):
        self.title = title
        self.theme = theme
        self.designer = designer

    def display_info(self):
        return f"Poster: '{self.title}' | Theme: {self.theme} | Designed by: {self.designer}"

    def celebrate(self):
        return f"🎉 '{self.title}' radiates {self.theme} energy! Designed with love by {self.designer}."

    def _str_(self):
        return f"CreativePoster(title='{self.title}', theme='{self.theme}', designer='{self.designer}')"

# Create an object of the class
poster1 = CreativePoster("Feisal's Birthday", "Basketball + Virgo Energy", "Khakky")

# Call methods
print(poster1.display_info())
print(poster1.celebrate())

# Print object to show _str_ output
print(poster1)