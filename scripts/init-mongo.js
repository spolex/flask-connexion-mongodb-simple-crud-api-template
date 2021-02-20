db.createUser({
  user: 'flask',
  pwd: 'flask',
  roles: [
    {
      role: 'readWrite',
      db: 'flaskdb'
    }
  ]
})