import http from 'k6/http';
import { sleep, check } from 'k6';
import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';

export default () => {
    const baseUrl = __ENV.BASE_URL;

    http.get(`${baseUrl}/users`);
    
    const randomUsername = uuidv4();
    http.post(`${baseUrl}/users`, `"${randomUsername}"`, {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    
    const response = http.get(`${baseUrl}/users/${randomUsername}`);
    check(response, {
        'New user has rank 0': (r) => r.json().rank === 0,
    });

    http.get(`${baseUrl}/games?username=${randomUsername}`);

    const gameInput = {
        challenger: randomUsername,
        opponent: "someone"
    }
    const createGameResponse = http.post(`${baseUrl}/games`, JSON.stringify(gameInput), {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const gameId = createGameResponse.json();

    const gameInfoResponse = http.get(`${baseUrl}/games/${gameId}`)
    check(gameInfoResponse, {
        'Fresh game has no moves': (r) => r.json().moves.length === 0,
        'Correct users in the game': (r) => r.json().playerA === 'someone' && r.json().playerB === randomUsername
    });

    const move = {
        x: 1,
        y: 1,
        occupier: 'A'
    }
    http.post(`${baseUrl}/games/${gameId}/moves`, JSON.stringify(move), {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    http.get(`${baseUrl}/games/${gameId}/winner`);
}
