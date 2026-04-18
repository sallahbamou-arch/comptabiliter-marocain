import React, { useState } from 'react';
import Dashboard from './Dashboard';
import Clients from './Clients';
import Documents from './Documents';
import Rapports from './Rapports';

const App = () => {
    const [activePage, setActivePage] = useState('Dashboard');

    const renderContent = () => {
        switch (activePage) {
            case 'Dashboard':
                return <Dashboard />;
            case 'Clients':
                return <Clients />;
            case 'Documents':
                return <Documents />;
            case 'Rapports':
                return <Rapports />;
            default:
                return <Dashboard />;
        }
    };

    return (
        <div>
            <header>
                <nav>
                    <button onClick={() => setActivePage('Dashboard')}>Dashboard</button>
                    <button onClick={() => setActivePage('Clients')}>Clients</button>
                    <button onClick={() => setActivePage('Documents')}>Documents</button>
                    <button onClick={() => setActivePage('Rapports')}>Rapports</button>
                </nav>
            </header>
            <main>
                {renderContent()}
            </main>
        </div>
    );
};

export default App;