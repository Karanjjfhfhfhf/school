from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace-with-secure-key'

admission_records = []
fee_notices = {
    'S1001': {'student': 'Anita Sharma', 'grade': '8', 'due': '₹12,500', 'due_date': '30 June 2026'},
    'S1002': {'student': 'Rahul Mehta', 'grade': '10', 'due': '₹14,200', 'due_date': '15 June 2026'},
    'S1003': {'student': 'Priya Singh', 'grade': '6', 'due': '₹11,800', 'due_date': '20 June 2026'},
}

@app.route('/')
def index():
    return render_template('index.html', admission_sent=False, fee_notice=None)

@app.route('/admission', methods=['POST'])
def submit_admission():
    applicant_name = request.form.get('name', '').strip()
    grade = request.form.get('grade', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    message = request.form.get('message', '').strip()

    admission_data = {
        'name': applicant_name,
        'grade': grade,
        'email': email,
        'phone': phone,
        'message': message,
    }
    admission_records.append(admission_data)

    return render_template(
        'index.html',
        admission_sent=True,
        admission_data=admission_data,
        fee_notice=None,
    )

@app.route('/fee-notice', methods=['POST'])
def fee_notice():
    student_id = request.form.get('student_id', '').strip().upper()
    notice = fee_notices.get(student_id)
    return render_template(
        'index.html',
        admission_sent=False,
        fee_notice=notice,
        student_id=student_id,
    )

if __name__ == '__main__':
    app.run(debug=True)
