class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def get_details(self):
        return f"Course: {self.course_name}\nDuration: {self.duration} weeks"


class WebDevClass(Course):
    def __init__(self, duration, framework):
        super().__init__("Web Development Fundamentals", duration)
        self.framework = framework

    def get_details(self):
        base_info = super().get_details()
        return (
            f"{base_info}\nFramework: {self.framework}\nIncludes: HTML, CSS, JavaScript"
        )


basic_course = Course("General Programming", 8)
print("Basic Course Details:")
print(basic_course.get_details())

print("\nWeb Development Course:")
web_course = WebDevClass(12, "React")
print(web_course.get_details())
