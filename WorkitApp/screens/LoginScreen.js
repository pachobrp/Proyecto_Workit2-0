
import { View, TextInput, Button, Alert } from 'react-native';
import React, { useState } from 'react';


export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    // Aquí hacés el fetch al backend con username y password
    try {
      const response = await fetch('http://192.168.100.28:3001/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });
      const data = await response.json();

      if (data.success) {
        // Navegás al Home pasando el username
        navigation.navigate('Home', { user: username });
      } else {
        Alert.alert('Error', 'Usuario o contraseña incorrectos');
      }
    } catch (error) {
      Alert.alert('Error', 'No se pudo conectar al servidor');
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <TextInput placeholder="Usuario" value={username} onChangeText={setUsername} />
      <TextInput placeholder="Contraseña" secureTextEntry value={password} onChangeText={setPassword} />
      <Button title="Iniciar sesión" onPress={handleLogin} />
    </View>
  );
}
