from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to calculate EMI
def calculate_emi(principal, rate, tenure):
    r = rate / (12 * 100)  # monthly interest rate
    emi = (principal * r * (1 + r) ** tenure) / ((1 + r) ** tenure - 1)
    return round(emi, 2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        principal = float(data['principal'])
        rate = float(data['rate'])
        tenure = int(data['tenure'])
        emi = calculate_emi(principal, rate, tenure)
        total_payment = round(emi * tenure, 2)
        total_interest = round(total_payment - principal, 2)
        return jsonify({
            'emi': emi,
            'total_payment': total_payment,
            'total_interest': total_interest
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
