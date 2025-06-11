from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

SECRET_KEY = 'your_secret_key_here'

def get_battery_percentage():
    try:
        output = subprocess.check_output(['termux-battery-status']).decode('utf-8')
        import json
        battery = json.loads(output)
        return battery.get('percentage', 'unknown')
    except Exception as e:
        return f'error: {str(e)}'

@app.route('/wake', methods=['POST'])
def wake():
    key = request.args.get('key')
    if key != SECRET_KEY:
        return jsonify({'status': 'unauthorized'}), 401

    os.system('wakeonlan 00:11:22:33:44:55')  # Replace with your PC's MAC address

    battery = get_battery_percentage()
    return jsonify({'status': 'WOL packet sent', 'battery': f'{battery}%'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#all of this is done with termux+tailscale for a phone server to wake on lan a pc