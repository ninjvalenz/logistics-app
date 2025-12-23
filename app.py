from flask import Flask, render_template, jsonify

app = Flask(__name__)


mock_packages = [
    {
        'id': 'PKG-2024-001',
        'trackingNumber': 'SF-2024-12-23-001',
        'status': 'in-transit',
        'origin': {'lat': 14.5995, 'lng': 120.9842, 'name': 'Manila Warehouse'},
        'destination': {'lat': 14.5764, 'lng': 121.0851, 'name': 'Quezon City Hub'},
        'currentLocation': {'lat': 14.5880, 'lng': 121.0350},
        'recipient': 'Juan Dela Cruz',
        'estimatedDelivery': '2024-12-23 15:00',
        'weight': '2.5 kg',
        'timeline': [
            {'time': '2024-12-23 08:00', 'status': 'Package picked up', 'location': 'Manila Warehouse', 'completed': True},
            {'time': '2024-12-23 09:30', 'status': 'In transit', 'location': 'Pasig Sorting Facility', 'completed': True},
            {'time': '2024-12-23 12:00', 'status': 'Out for delivery', 'location': 'En route to destination', 'completed': True},
            {'time': '2024-12-23 14:30', 'status': 'Arrived at destination', 'location': 'Quezon City Hub', 'completed': False},
            {'time': '2024-12-23 15:00', 'status': 'Delivered', 'location': 'Quezon City Hub - Received by recipient', 'completed': False}
        ]
    },
    {
        'id': 'PKG-2024-002',
        'trackingNumber': 'SF-2024-12-23-002',
        'status': 'in-transit',
        'origin': {'lat': 10.3157, 'lng': 123.8854, 'name': 'Cebu Hub'},
        'destination': {'lat': 14.5995, 'lng': 120.9842, 'name': 'Manila Warehouse'},
        'currentLocation': {'lat': 12.3456, 'lng': 122.2345},
        'recipient': 'Maria Santos',
        'estimatedDelivery': '2024-12-23 18:00',
        'weight': '5.0 kg',
        'timeline': [
            {'time': '2024-12-23 07:00', 'status': 'Package picked up', 'location': 'Cebu Hub', 'completed': True},
            {'time': '2024-12-23 10:00', 'status': 'In sorting facility', 'location': 'Cebu Sorting Center', 'completed': True},
            {'time': '2024-12-23 14:00', 'status': 'In transit', 'location': 'En route to Manila', 'completed': False},
            {'time': '2024-12-23 17:00', 'status': 'Arrived at destination', 'location': 'Manila Warehouse', 'completed': False},
            {'time': '2024-12-23 18:00', 'status': 'Ready for pickup', 'location': 'Manila Warehouse', 'completed': False}
        ]
    },
    {
        'id': 'PKG-2024-003',
        'trackingNumber': 'SF-2024-12-23-003',
        'status': 'in-transit',
        'origin': {'lat': 7.0731, 'lng': 125.6128, 'name': 'Davao Center'},
        'destination': {'lat': 10.3157, 'lng': 123.8854, 'name': 'Cebu Hub'},
        'currentLocation': {'lat': 8.9539, 'lng': 125.5281},
        'recipient': 'Pedro Reyes',
        'estimatedDelivery': '2024-12-23 20:00',
        'weight': '1.2 kg',
        'timeline': [
            {'time': '2024-12-23 09:00', 'status': 'Package picked up', 'location': 'Davao Center', 'completed': True},
            {'time': '2024-12-23 13:00', 'status': 'In transit', 'location': 'En route to Cebu', 'completed': False},
            {'time': '2024-12-23 18:00', 'status': 'Arrived at destination', 'location': 'Cebu Hub', 'completed': False},
            {'time': '2024-12-23 20:00', 'status': 'Delivered', 'location': 'Cebu Hub - Received by recipient', 'completed': False}
        ]
    }
]


all_shipments = [
    {
        'id': 'PKG-2024-001',
        'trackingNumber': 'SF-2024-12-23-001',
        'status': 'in-transit',
        'origin': 'Manila Warehouse',
        'destination': 'Quezon City Hub',
        'recipient': 'Juan Dela Cruz',
        'estimatedDelivery': '2024-12-23 15:00',
        'weight': '2.5 kg',
        'currentStatus': 'Out for delivery',
        'priority': 'Standard'
    },
    {
        'id': 'PKG-2024-002',
        'trackingNumber': 'SF-2024-12-23-002',
        'status': 'in-transit',
        'origin': 'Cebu Hub',
        'destination': 'Manila Warehouse',
        'recipient': 'Maria Santos',
        'estimatedDelivery': '2024-12-23 18:00',
        'weight': '5.0 kg',
        'currentStatus': 'In sorting facility',
        'priority': 'Express'
    },
    {
        'id': 'PKG-2024-003',
        'trackingNumber': 'SF-2024-12-23-003',
        'status': 'in-transit',
        'origin': 'Davao Center',
        'destination': 'Cebu Hub',
        'recipient': 'Pedro Reyes',
        'estimatedDelivery': '2024-12-23 20:00',
        'weight': '1.2 kg',
        'currentStatus': 'In transit',
        'priority': 'Standard'
    },
    {
        'id': 'PKG-2024-004',
        'trackingNumber': 'SF-2024-12-23-004',
        'status': 'pending',
        'origin': 'Manila Warehouse',
        'destination': 'Baguio Station',
        'recipient': 'Ana Garcia',
        'estimatedDelivery': '2024-12-24 10:00',
        'weight': '3.8 kg',
        'currentStatus': 'Pending pickup',
        'priority': 'Express'
    },
    {
        'id': 'PKG-2024-005',
        'trackingNumber': 'SF-2024-12-23-005',
        'status': 'in-transit',
        'origin': 'Quezon City Hub',
        'destination': 'Makati Office',
        'recipient': 'Carlos Tan',
        'estimatedDelivery': '2024-12-23 14:00',
        'weight': '0.8 kg',
        'currentStatus': 'Out for delivery',
        'priority': 'Express'
    },
    {
        'id': 'PKG-2024-006',
        'trackingNumber': 'SF-2024-12-23-006',
        'status': 'in-transit',
        'origin': 'Iloilo Depot',
        'destination': 'Manila Warehouse',
        'recipient': 'Linda Cruz',
        'estimatedDelivery': '2024-12-23 22:00',
        'weight': '4.5 kg',
        'currentStatus': 'In transit',
        'priority': 'Standard'
    },
    {
        'id': 'PKG-2024-007',
        'trackingNumber': 'SF-2024-12-23-007',
        'status': 'delivered',
        'origin': 'Manila Warehouse',
        'destination': 'Pasig Hub',
        'recipient': 'Robert Lee',
        'estimatedDelivery': '2024-12-23 10:00',
        'weight': '2.0 kg',
        'currentStatus': 'Delivered',
        'priority': 'Standard'
    },
    {
        'id': 'PKG-2024-008',
        'trackingNumber': 'SF-2024-12-23-008',
        'status': 'in-transit',
        'origin': 'Cagayan de Oro Hub',
        'destination': 'Davao Center',
        'recipient': 'Sofia Martinez',
        'estimatedDelivery': '2024-12-23 19:00',
        'weight': '6.2 kg',
        'currentStatus': 'In sorting facility',
        'priority': 'Express'
    },
    {
        'id': 'PKG-2024-009',
        'trackingNumber': 'SF-2024-12-23-009',
        'status': 'in-transit',
        'origin': 'Manila Warehouse',
        'destination': 'Laguna Station',
        'recipient': 'Michael Wong',
        'estimatedDelivery': '2024-12-23 16:00',
        'weight': '1.5 kg',
        'currentStatus': 'Out for delivery',
        'priority': 'Standard'
    },
    {
        'id': 'PKG-2024-010',
        'trackingNumber': 'SF-2024-12-23-010',
        'status': 'pending',
        'origin': 'Cebu Hub',
        'destination': 'Iloilo Depot',
        'recipient': 'Grace Lim',
        'estimatedDelivery': '2024-12-24 08:00',
        'weight': '3.2 kg',
        'currentStatus': 'Pending pickup',
        'priority': 'Standard'
    }
]


mock_inventory = [
    {'id': 1, 'name': 'Laptop Computer', 'sku': 'ELEC-001', 'quantity': 45, 'location': 'Warehouse A - Section 2', 'category': 'Electronics', 'status': 'high'},
    {'id': 2, 'name': 'Office Chair', 'sku': 'FURN-012', 'quantity': 120, 'location': 'Warehouse B - Section 5', 'category': 'Furniture', 'status': 'high'},
    {'id': 3, 'name': 'Smartphone', 'sku': 'ELEC-089', 'quantity': 23, 'location': 'Warehouse A - Section 1', 'category': 'Electronics', 'status': 'medium'},
    {'id': 4, 'name': 'Desk Lamp', 'sku': 'FURN-034', 'quantity': 8, 'location': 'Warehouse C - Section 3', 'category': 'Furniture', 'status': 'low'},
    {'id': 5, 'name': 'Wireless Mouse', 'sku': 'ELEC-045', 'quantity': 67, 'location': 'Warehouse A - Section 2', 'category': 'Electronics', 'status': 'high'},
    {'id': 6, 'name': 'Monitor Stand', 'sku': 'FURN-078', 'quantity': 15, 'location': 'Warehouse B - Section 4', 'category': 'Furniture', 'status': 'medium'},
    {'id': 7, 'name': 'USB Hub', 'sku': 'ELEC-123', 'quantity': 5, 'location': 'Warehouse A - Section 3', 'category': 'Electronics', 'status': 'low'},
    {'id': 8, 'name': 'Ergonomic Keyboard', 'sku': 'ELEC-067', 'quantity': 34, 'location': 'Warehouse A - Section 1', 'category': 'Electronics', 'status': 'high'},
]

@app.route('/')
def index():
    return render_template('tracking.html')

@app.route('/tracking')
def tracking():
    return render_template('tracking.html')

@app.route('/shipments')
def shipments():
    return render_template('shipments.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')


@app.route('/api/packages')
def api_packages():
    return jsonify(mock_packages)

@app.route('/api/shipments')
def api_shipments():
    return jsonify(all_shipments)

@app.route('/api/inventory')
def api_inventory():
    return jsonify(mock_inventory)

app_handler = app
