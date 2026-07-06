export default function updateGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students) || !Array.isArray(newGrades)) {
        return [];
    }
    return students.map((student) => {
        if (student.location === city) {
            if (!student.hasOwnProperty('grade')) {
                student.grade = 'N/A';
            }
            const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
            if (gradeObj) {
                return { ...student, grade: gradeObj.grade };
            }
        }
        return student;
    });
}