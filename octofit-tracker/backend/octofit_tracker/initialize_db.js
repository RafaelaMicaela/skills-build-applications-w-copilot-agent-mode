// initialize_db.js

const { MongoClient } = require('mongodb');

async function initializeDatabase() {
    const uri = 'mongodb://localhost:27017';
    const client = new MongoClient(uri);

    try {
        await client.connect();
        const db = client.db('octofit_db');

        // Create collections and indexes
        await db.createCollection('users');
        await db.collection('users').createIndex({ email: 1 }, { unique: true });

        await db.createCollection('teams');
        await db.createCollection('activities');
        await db.createCollection('leaderboard');
        await db.createCollection('workouts');

        console.log('Database initialized successfully.');
    } catch (error) {
        console.error('Error initializing database:', error);
    } finally {
        await client.close();
    }
}

initializeDatabase();
