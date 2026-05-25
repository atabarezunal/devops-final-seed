def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    
def test_get_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    
def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Test",
            "description": "Testing"
        }
    )

    data = response.get_json()

    assert response.status_code == 201
    assert data["title"] == "Test"

def test_update_task(client):
    created = client.post(
        "/tasks",
        json={
            "title": "Old"
        }
    )

    task = created.get_json()

    response = client.put(
        f"/tasks/{task['id']}",
        json={
            "title": "New"
        }
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["title"] == "New"
    
def test_delete_task(client):
    created = client.post(
        "/tasks",
        json={
            "title": "Delete me"
        }
    )

    task = created.get_json()

    response = client.delete(f"/tasks/{task['id']}")

    assert response.status_code == 200