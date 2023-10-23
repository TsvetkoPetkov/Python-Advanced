def gather_credits(number_of_needed_credits, *args):
    all_courses = []
    total_credits = 0

    for course_info in args:
        course_name, course_credits = course_info
        if course_name in all_courses:
            continue
        else:
            if total_credits < number_of_needed_credits:
                total_credits += course_credits
                all_courses.append(course_name)
            else:
                break

    sorted_courses = sorted(all_courses)

    if total_credits >= number_of_needed_credits:
        return f"Enrollment finished! Maximum credits: {total_credits}.\n" \
               f"Courses: {', '.join(sorted_courses)}"
    else:
        return f"You need to enroll in more courses! You have to gather {number_of_needed_credits - total_credits} credits more."
