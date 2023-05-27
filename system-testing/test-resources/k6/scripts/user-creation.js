import http from 'k6/http';
import { sleep, check } from 'k6';
import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';

export default () => {
    http.get(`${__ENV.BASE_URL}/users`);
    
    const randomUsername = uuidv4();
    http.post(`${__ENV.BASE_URL}/users`, `"${randomUsername}"`, {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    
    const response = http.get(`${__ENV.BASE_URL}/users/${randomUsername}`);
    check(response, {
        'New user has rank 0': (r) => r.json().rank === 0,
    });

    sleep(1);
}