import random
from datetime import datetime, timedelta

def get_dashboard_metrics():
    """Generate enhanced synthetic dashboard metrics"""
    return {
        'total_routes': 156,
        'active_drivers': 23,
        'fuel_efficiency': 8.5,
        'cost_savings': 15.2,
        'avg_delivery_time': '4h 25min',
        'monthly_fuel_cost': 45780.50,
        'routes_completed_today': 12,
        'pending_routes': 8,
        'fuel_prices': {
            'gasolina_comum': 5.89,
            'gasolina_aditivada': 6.15,
            'diesel_s10': 5.45,
            'vale_gasolina': 5.95
        },
        # Enhanced metrics for advanced dashboard
        'kpis': {
            'punctuality': 94.2,
            'customer_satisfaction': 4.7,
            'fleet_utilization': 87.5,
            'energy_efficiency': 8.7,
            'safety_score': 96.3,
            'maintenance_compliance': 89.1
        },
        'real_time_operations': [
            {
                'route_id': 'SP-RJ-1247',
                'driver': 'João Silva',
                'progress': 65,
                'eta': '14:30',
                'status': 'active',
                'alerts': []
            },
            {
                'route_id': 'CWB-SP-1248',
                'driver': 'Maria Santos',
                'progress': 45,
                'eta': '16:15',
                'status': 'warning',
                'alerts': ['heavy_rain']
            },
            {
                'route_id': 'BH-RJ-1246',
                'driver': 'Carlos Oliveira',
                'progress': 100,
                'eta': 'Concluída',
                'status': 'completed',
                'alerts': []
            }
        ],
        'alerts': [
            {
                'id': 1,
                'type': 'maintenance',
                'severity': 'high',
                'title': 'Manutenção Urgente',
                'message': 'Veículo ABC-1234 precisa de manutenção imediata',
                'timestamp': datetime.now() - timedelta(minutes=15),
                'acknowledged': False
            },
            {
                'id': 2,
                'type': 'weather',
                'severity': 'medium',
                'title': 'Condições Climáticas',
                'message': 'Chuva forte prevista na rota BR-116',
                'timestamp': datetime.now() - timedelta(minutes=32),
                'acknowledged': False
            },
            {
                'id': 3,
                'type': 'achievement',
                'severity': 'low',
                'title': 'Economia de Combustível',
                'message': 'Meta mensal de economia atingida',
                'timestamp': datetime.now() - timedelta(hours=1),
                'acknowledged': True
            }
        ],
        'performance_trends': {
            'hourly_routes': [2, 1, 8, 15, 12, 6],
            'efficiency_trend': [85, 87, 92, 89, 94, 91],
            'fuel_price_history': {
                'gasolina': [5.95, 5.92, 5.89, 5.91, 5.89, 5.87, 5.89],
                'diesel': [5.52, 5.48, 5.45, 5.47, 5.45, 5.43, 5.45]
            }
        }
    }

def get_drivers_data():
    """Generate enhanced synthetic driver data with comprehensive metrics"""
    drivers = []
    names = ['João Silva', 'Maria Santos', 'Carlos Oliveira', 'Ana Costa', 'Pedro Almeida', 
             'Lucia Ferreira', 'Roberto Lima', 'Fernanda Souza', 'Marcos Pereira', 'Julia Rodrigues',
             'Ricardo Barbosa', 'Camila Nunes', 'Diego Martins', 'Patrícia Gomes', 'André Vieira',
             'Beatriz Campos', 'Thiago Rocha', 'Vanessa Dias', 'Felipe Cardoso', 'Renata Moura']
    
    for i, name in enumerate(names):
        avg_consumption = round(random.uniform(7.5, 12.0), 2)
        km_driven = random.randint(15000, 45000)
        efficiency_score = random.randint(75, 98)
        
        drivers.append({
            'id': i + 1,
            'name': name,
            'avg_consumption': avg_consumption,
            'km_driven': km_driven,
            'efficiency_score': efficiency_score,
            'penalties': random.randint(0, 3),
            'bonuses': random.randint(0, 5),
            'status': random.choice(['Ativo', 'Em Rota', 'Descanso']),
            # Enhanced driver metrics
            'license_number': f'CNH{random.randint(100000000, 999999999)}',
            'hire_date': datetime.now() - timedelta(days=random.randint(30, 1825)),
            'experience_years': random.randint(2, 15),
            'safety_score': random.randint(80, 100),
            'punctuality_score': random.randint(85, 100),
            'training_completed': random.randint(60, 100),
            'monthly_performance': {
                'routes_completed': random.randint(15, 35),
                'fuel_savings': round(random.uniform(-5.0, 15.0), 2),
                'customer_rating': round(random.uniform(4.0, 5.0), 1),
                'incidents': random.randint(0, 2),
                'overtime_hours': random.randint(0, 20)
            },
            'performance_history': [
                {'month': 'Jan', 'consumption': round(avg_consumption + random.uniform(-0.5, 0.5), 2), 'efficiency': efficiency_score + random.randint(-5, 5)},
                {'month': 'Fev', 'consumption': round(avg_consumption + random.uniform(-0.5, 0.5), 2), 'efficiency': efficiency_score + random.randint(-5, 5)},
                {'month': 'Mar', 'consumption': round(avg_consumption + random.uniform(-0.5, 0.5), 2), 'efficiency': efficiency_score + random.randint(-5, 5)},
                {'month': 'Abr', 'consumption': round(avg_consumption + random.uniform(-0.5, 0.5), 2), 'efficiency': efficiency_score + random.randint(-5, 5)},
                {'month': 'Mai', 'consumption': round(avg_consumption + random.uniform(-0.5, 0.5), 2), 'efficiency': efficiency_score + random.randint(-5, 5)},
                {'month': 'Jun', 'consumption': avg_consumption, 'efficiency': efficiency_score}
            ],
            'certifications': random.sample(['Direção Defensiva', 'Transporte de Cargas Perigosas', 'Primeiros Socorros', 'Economia de Combustível'], random.randint(1, 3)),
            'vehicle_assigned': f'ABC-{1234 + (i % 10)}',
            'contact': {
                'phone': f'(41) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}',
                'email': f'{name.lower().replace(" ", ".")}@wiseroutes.com'
            },
            'emergency_contact': {
                'name': f'Contato de {name.split()[0]}',
                'phone': f'(41) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}'
            }
        })
    
    return drivers

def get_driver_analytics():
    """Generate driver analytics and education data"""
    return {
        'best_driver': {
            'name': 'João Silva',
            'avg_consumption': 11.2,
            'efficiency_score': 95,
            'fuel_savings': 12.5
        },
        'fuel_savings': 2847.50,
        'efficiency_target': 90,
        'drivers_meeting_target': 12,
        'training_modules': [
            {
                'id': 1,
                'name': 'Direção Econômica',
                'description': 'Técnicas para reduzir consumo em até 20%',
                'duration': '2 horas',
                'completion_rate': 75,
                'participants': 15,
                'total_drivers': 20,
                'topics': ['Aceleração suave', 'Manutenção de velocidade', 'Uso do freio motor', 'Planejamento de rotas']
            },
            {
                'id': 2,
                'name': 'Planejamento de Rotas',
                'description': 'Otimização de trajetos e economia de tempo',
                'duration': '1.5 horas',
                'completion_rate': 60,
                'participants': 12,
                'total_drivers': 20,
                'topics': ['Análise de tráfego', 'Rotas alternativas', 'Horários de pico', 'Uso de GPS']
            },
            {
                'id': 3,
                'name': 'Manutenção Preventiva',
                'description': 'Cuidados básicos para melhor performance',
                'duration': '3 horas',
                'completion_rate': 40,
                'participants': 8,
                'total_drivers': 20,
                'topics': ['Verificação de pneus', 'Níveis de fluidos', 'Filtros', 'Inspeção visual']
            }
        ],
        'reward_system': {
            'fuel_economy': {
                'bonus_per_percent': 50.00,
                'eligible_drivers': 12,
                'total_bonuses': 2400.00,
                'criteria': 'Economia de 5% acima da meta'
            },
            'punctuality': {
                'bonus_per_delivery': 30.00,
                'eligible_drivers': 8,
                'total_bonuses': 960.00,
                'criteria': 'Entregas pontuais sem atrasos'
            },
            'safety': {
                'monthly_bonus': 100.00,
                'eligible_drivers': 18,
                'total_bonuses': 1800.00,
                'criteria': 'Sem infrações ou acidentes'
            }
        },
        'efficiency_tips': [
            {
                'category': 'Velocidade',
                'tip': 'Mantenha velocidade entre 80-90 km/h para máxima eficiência',
                'savings_potential': '15%'
            },
            {
                'category': 'Aquecimento',
                'tip': 'Evite acelerar bruscamente nos primeiros 5 minutos',
                'savings_potential': '8%'
            },
            {
                'category': 'Ar Condicionado',
                'tip': 'Use ar condicionado acima de 60 km/h, janelas abertas em baixa velocidade',
                'savings_potential': '10%'
            },
            {
                'category': 'Peso',
                'tip': 'Remova itens desnecessários - cada 50kg extras aumentam 2% o consumo',
                'savings_potential': '5%'
            }
        ]
    }

def get_vehicles_data():
    """Generate synthetic vehicle data"""
    vehicles = []
    models = ['Volvo FH', 'Scania R450', 'Mercedes Actros', 'Iveco Stralis', 'DAF XF']
    
    for i, model in enumerate(models):
        vehicles.append({
            'id': i + 1,
            'model': model,
            'plate': f'ABC-{1234 + i}',
            'fuel_type': random.choice(['Diesel S10', 'Gasolina']),
            'avg_consumption': round(random.uniform(2.8, 4.2), 2),
            'cargo_capacity': random.randint(15000, 30000),
            'maintenance_cost': random.randint(2500, 8000),
            'status': random.choice(['Disponível', 'Em Uso', 'Manutenção'])
        })
    
    return vehicles

def get_routes_data():
    """Generate synthetic route data"""
    routes = []
    cities = [
        {'name': 'Curitiba', 'lat': -25.4284, 'lng': -49.2733},
        {'name': 'São Paulo', 'lat': -23.5505, 'lng': -46.6333},
        {'name': 'Rio de Janeiro', 'lat': -22.9068, 'lng': -43.1729},
        {'name': 'Belo Horizonte', 'lat': -19.9167, 'lng': -43.9345},
        {'name': 'Porto Alegre', 'lat': -30.0346, 'lng': -51.2177}
    ]
    
    for i in range(10):
        origin = random.choice(cities)
        destination = random.choice([c for c in cities if c != origin])
        
        routes.append({
            'id': i + 1,
            'origin': origin,
            'destination': destination,
            'distance': random.randint(200, 800),
            'estimated_time': f"{random.randint(3, 12)}h {random.randint(0, 59)}min",
            'fuel_cost': round(random.uniform(150, 600), 2),
            'cargo_weight': random.randint(5000, 25000),
            'status': random.choice(['Planejada', 'Em Andamento', 'Concluída'])
        })
    
    return routes

def get_weather_data():
    """Generate synthetic weather data"""
    cities = ['Curitiba', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
    conditions = ['Ensolarado', 'Parcialmente Nublado', 'Nublado', 'Chuva Leve', 'Chuva Forte']
    
    weather = []
    for city in cities:
        weather.append({
            'city': city,
            'temperature': random.randint(15, 35),
            'condition': random.choice(conditions),
            'humidity': random.randint(40, 90),
            'wind_speed': random.randint(5, 25),
            'visibility': random.choice(['Boa', 'Moderada', 'Ruim']),
            'alerts': random.choice([[], ['Chuva Forte'], ['Neblina'], ['Vento Forte']])
        })
    
    return weather

def get_cost_analysis():
    """Generate synthetic cost analysis data"""
    return {
        'operational_costs': {
            'fuel': 45780.50,
            'maintenance': 12500.00,
            'tolls': 8900.00,
            'insurance': 3200.00,
            'driver_salaries': 28000.00
        },
        'cost_per_km': 2.85,
        'monthly_savings': 15.2,
        'electric_vehicle_analysis': {
            'initial_investment': 450000.00,
            'monthly_energy_cost': 8500.00,
            'payback_period': '3.2 anos',
            'co2_reduction': '65%'
        },
        'efficiency_trends': [
            {'month': 'Jan', 'efficiency': 8.2},
            {'month': 'Fev', 'efficiency': 8.5},
            {'month': 'Mar', 'efficiency': 8.8},
            {'month': 'Abr', 'efficiency': 8.6},
            {'month': 'Mai', 'efficiency': 9.1}
        ]
    }
