from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime, timedelta
from data.synthetic_data import (
    get_dashboard_metrics, get_drivers_data, get_vehicles_data,
    get_routes_data, get_weather_data, get_cost_analysis, get_driver_analytics
)

app = Flask(__name__)

@app.route('/')
def dashboard():
    metrics = get_dashboard_metrics()
    return render_template('dashboard.html', metrics=metrics)

@app.route('/map')
def map_view():
    routes = get_routes_data()
    return render_template('map.html', routes=routes)

@app.route('/drivers')
def drivers():
    drivers_data = get_drivers_data()
    analytics = get_driver_analytics()
    return render_template('drivers.html', 
                         drivers=drivers_data,
                         best_driver=analytics['best_driver'],
                         fuel_savings=analytics['fuel_savings'],
                         efficiency_target=analytics['efficiency_target'],
                         drivers_meeting_target=analytics['drivers_meeting_target'])

@app.route('/vehicles')
def vehicles():
    vehicles_data = get_vehicles_data()
    return render_template('vehicles.html', vehicles=vehicles_data)

@app.route('/costs')
def costs():
    cost_data = get_cost_analysis()
    return render_template('costs.html', costs=cost_data)

@app.route('/weather')
def weather():
    weather_data = get_weather_data()
    return render_template('weather.html', weather=weather_data)

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/api/driver/<int:driver_id>')
def get_driver_details(driver_id):
    """Get detailed information about a specific driver"""
    drivers = get_drivers_data()
    driver = next((d for d in drivers if d['id'] == driver_id), None)
    
    if not driver:
        return jsonify({'error': 'Driver not found'}), 404
    
    return jsonify(driver)

@app.route('/api/driver/<int:driver_id>/performance')
def get_driver_performance(driver_id):
    """Get performance analytics for a specific driver"""
    drivers = get_drivers_data()
    driver = next((d for d in drivers if d['id'] == driver_id), None)
    
    if not driver:
        return jsonify({'error': 'Driver not found'}), 404
    
    # Enhanced performance data
    performance_data = {
        'driver_id': driver_id,
        'name': driver['name'],
        'current_metrics': {
            'avg_consumption': driver['avg_consumption'],
            'efficiency_score': driver['efficiency_score'],
            'km_driven': driver['km_driven'],
            'safety_score': driver['safety_score'],
            'punctuality_score': driver['punctuality_score']
        },
        'monthly_performance': driver['monthly_performance'],
        'performance_history': driver['performance_history'],
        'certifications': driver['certifications'],
        'recommendations': [
            'Manter velocidade constante entre 80-90 km/h',
            'Evitar acelerações bruscas nos primeiros 5 minutos',
            'Realizar manutenção preventiva regularmente'
        ],
        'goals': {
            'fuel_efficiency': driver['avg_consumption'] + 0.5,
            'safety_target': min(driver['safety_score'] + 2, 100),
            'training_completion': 100
        }
    }
    
    return jsonify(performance_data)

@app.route('/api/drivers/analytics')
def get_drivers_analytics():
    """Get comprehensive driver analytics and statistics"""
    analytics = get_driver_analytics()
    return jsonify(analytics)

@app.route('/api/drivers/training')
def get_training_modules():
    """Get available training modules and completion status"""
    analytics = get_driver_analytics()
    return jsonify({
        'modules': analytics['training_modules'],
        'completion_stats': {
            'total_modules': len(analytics['training_modules']),
            'avg_completion': sum(m['completion_rate'] for m in analytics['training_modules']) / len(analytics['training_modules'])
        }
    })

@app.route('/api/drivers/rewards')
def get_reward_system():
    """Get reward system information and statistics"""
    analytics = get_driver_analytics()
    return jsonify(analytics['reward_system'])

@app.route('/api/drivers/tips')
def get_efficiency_tips():
    """Get fuel efficiency tips and recommendations"""
    analytics = get_driver_analytics()
    return jsonify({
        'tips': analytics['efficiency_tips'],
        'total_savings_potential': '38%'
    })

@app.route('/api/driver/assign-route', methods=['POST'])
def assign_route_to_driver():
    """Assign a route to a specific driver"""
    data = request.get_json()
    
    assignment = {
        'assignment_id': f"assign_{hash(str(data)) % 10000}",
        'driver_id': data.get('driver_id'),
        'route_id': data.get('route_id'),
        'scheduled_date': data.get('scheduled_date'),
        'estimated_duration': data.get('estimated_duration'),
        'cargo_details': data.get('cargo_details'),
        'special_instructions': data.get('special_instructions', ''),
        'status': 'scheduled',
        'created_at': datetime.now().isoformat()
    }
    
    return jsonify({
        'success': True,
        'assignment': assignment,
        'message': 'Rota atribuída com sucesso'
    })

@app.route('/api/driver/<int:driver_id>/schedule')
def get_driver_schedule(driver_id):
    """Get driver's schedule and assignments"""
    import random
    
    # Generate sample schedule data
    schedule = []
    for i in range(7):  # Next 7 days
        date = datetime.now() + timedelta(days=i)
        if random.random() < 0.7:  # 70% chance of having assignment
            schedule.append({
                'date': date.strftime('%Y-%m-%d'),
                'route': f'Rota {random.choice(["SP-RJ", "CWB-SP", "BH-RJ"])}',
                'start_time': f'{random.randint(6, 10):02d}:00',
                'estimated_duration': f'{random.randint(4, 8)}h {random.randint(0, 59)}min',
                'status': random.choice(['scheduled', 'in_progress', 'completed'])
            })
    
    return jsonify({
        'driver_id': driver_id,
        'schedule': schedule,
        'total_assignments': len(schedule)
    })

@app.route('/api/drivers/leaderboard')
def get_drivers_leaderboard():
    """Get driver performance leaderboard"""
    drivers = get_drivers_data()
    
    # Sort drivers by efficiency score
    leaderboard = sorted(drivers, key=lambda x: x['efficiency_score'], reverse=True)[:10]
    
    for i, driver in enumerate(leaderboard):
        driver['rank'] = i + 1
        driver['badge'] = 'gold' if i < 3 else 'silver' if i < 6 else 'bronze'
    
    return jsonify({
        'leaderboard': leaderboard,
        'categories': ['efficiency_score', 'avg_consumption', 'safety_score', 'punctuality_score']
    })

# API endpoints
@app.route('/api/route-optimization', methods=['POST'])
def optimize_route():
    data = request.get_json()
    
    # Enhanced route optimization with multiple algorithms
    origin = data.get('origin', '')
    destination = data.get('destination', '')
    vehicle_id = data.get('vehicle', '')
    cargo_weight = data.get('cargoWeight', 0)
    optimization_type = data.get('optimizationType', 'fastest')
    avoid_tolls = data.get('avoidTolls', False)
    
    # Simulate advanced route calculation
    base_distance = 450.5
    base_duration = 390  # minutes
    base_fuel_cost = 285.75
    
    # Apply optimization factors
    if optimization_type == 'economical':
        base_distance *= 1.1  # Longer but more economical route
        base_duration *= 1.15
        base_fuel_cost *= 0.85
    elif optimization_type == 'shortest':
        base_distance *= 0.9
        base_duration *= 1.05
        base_fuel_cost *= 0.95
    
    if avoid_tolls:
        base_distance *= 1.2
        base_duration *= 1.3
        base_fuel_cost *= 0.9  # No toll costs
    
    # Weight factor
    weight_factor = 1 + (cargo_weight / 30000) * 0.2
    base_fuel_cost *= weight_factor
    
    optimized_route = {
        'route_id': f"route_{hash(f'{origin}{destination}') % 10000}",
        'distance': round(base_distance, 1),
        'duration_minutes': int(base_duration),
        'duration_formatted': f"{int(base_duration // 60)}h {int(base_duration % 60)}min",
        'fuel_cost': round(base_fuel_cost, 2),
        'toll_cost': 0 if avoid_tolls else round(base_distance * 0.15, 2),
        'total_cost': round(base_fuel_cost + (0 if avoid_tolls else base_distance * 0.15), 2),
        'optimization_type': optimization_type,
        'waypoints': [
            {'lat': -25.4284, 'lng': -49.2733, 'name': 'Curitiba', 'type': 'origin'},
            {'lat': -24.5, 'lng': -48.5, 'name': 'Ponto Intermediário', 'type': 'waypoint'},
            {'lat': -23.5505, 'lng': -46.6333, 'name': 'São Paulo', 'type': 'destination'}
        ],
        'traffic_conditions': 'moderate',
        'weather_impact': 'minimal',
        'estimated_fuel_consumption': round(base_distance / 8.5, 1)
    }
    
    return jsonify(optimized_route)

@app.route('/api/route-alternatives', methods=['POST'])
def get_route_alternatives():
    data = request.get_json()
    
    # Generate multiple route alternatives
    alternatives = []
    base_routes = [
        {'name': 'Rota Rápida', 'type': 'fastest', 'distance': 420, 'duration': 360, 'cost': 275},
        {'name': 'Rota Econômica', 'type': 'economical', 'distance': 485, 'duration': 420, 'cost': 245},
        {'name': 'Rota Sem Pedágios', 'type': 'no_tolls', 'distance': 510, 'duration': 450, 'cost': 260}
    ]
    
    for i, route in enumerate(base_routes):
        alternatives.append({
            'id': f"alt_{i+1}",
            'name': route['name'],
            'distance': route['distance'],
            'duration_formatted': f"{route['duration']//60}h {route['duration']%60}min",
            'fuel_cost': route['cost'],
            'toll_cost': 0 if route['type'] == 'no_tolls' else round(route['distance'] * 0.12, 2),
            'total_cost': route['cost'] + (0 if route['type'] == 'no_tolls' else round(route['distance'] * 0.12, 2)),
            'traffic_level': ['low', 'moderate', 'high'][i],
            'recommended': i == 0
        })
    
    return jsonify({'alternatives': alternatives})

@app.route('/api/live-tracking/<route_id>')
def get_live_tracking(route_id):
    # Simulate live tracking data
    import random
    
    tracking_data = {
        'route_id': route_id,
        'current_position': {
            'lat': -24.8 + random.uniform(-0.5, 0.5),
            'lng': -48.2 + random.uniform(-0.5, 0.5)
        },
        'progress_percentage': random.randint(15, 85),
        'estimated_arrival': '14:30',
        'current_speed': random.randint(60, 90),
        'fuel_remaining': random.randint(40, 80),
        'driver_status': random.choice(['driving', 'break', 'loading']),
        'alerts': []
    }
    
    # Add random alerts
    if random.random() < 0.3:
        tracking_data['alerts'].append({
            'type': 'traffic',
            'message': 'Trânsito intenso detectado à frente',
            'severity': 'medium'
        })
    
    return jsonify(tracking_data)

@app.route('/api/waypoints', methods=['POST'])
def manage_waypoints():
    data = request.get_json()
    action = data.get('action')
    
    if action == 'add':
        waypoint = {
            'id': f"wp_{hash(str(data)) % 10000}",
            'lat': data.get('lat'),
            'lng': data.get('lng'),
            'name': data.get('name', 'Ponto de Parada'),
            'type': data.get('type', 'stop'),
            'duration_minutes': data.get('duration', 15)
        }
        return jsonify({'success': True, 'waypoint': waypoint})
    
    elif action == 'remove':
        waypoint_id = data.get('waypoint_id')
        return jsonify({'success': True, 'removed_id': waypoint_id})
    
    return jsonify({'success': False, 'error': 'Invalid action'})

@app.route('/api/fuel-prices')
def fuel_prices():
    return jsonify({
        'gasolina_comum_curitiba': 5.89,
        'gasolina_aditivada_curitiba': 6.15,
        'diesel_s10': 5.45,
        'vale_gasolina_interestadual': 5.95
    })

if __name__ == '__main__':
    app.run(debug=True)
