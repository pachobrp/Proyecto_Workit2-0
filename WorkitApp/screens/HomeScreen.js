import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function HomeScreen({ route, navigation }) {
  const { user } = route.params;

  const handleLogout = () => {
    // Si usas token en AsyncStorage, borralo acá también
    navigation.replace('Login');
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>¡Bienvenido a Work.it, {user}!</Text>
      </View>

      <View style={styles.content}>
        <Text style={styles.paragraph}>Has iniciado sesión correctamente.</Text>
        <Text style={styles.paragraph}>Objetivos del Sprint Nº 1:</Text>
        <View style={styles.list}>
          <Text>📝 Un formulario de login (usuario).</Text>
          <Text>🔗 Comunicación con backend.</Text>
          <Text>✅ Validación simple de usuario.</Text>
          <Text>🔐 Manejo de sesión (token o variable simple).</Text>
          <Text>➡️ Redirección al "Home" si el login es exitoso.</Text>
        </View>
      </View>

      <View style={styles.footer}>
        <Button title="🔓 Cerrar sesión" color="#dc3545" onPress={handleLogout} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f9f9fb' },
  header: { marginBottom: 20 },
  title: { fontSize: 22, fontWeight: 'bold', color: '#333' },
  content: { backgroundColor: '#e6f0fa', padding: 15, borderRadius: 8 },
  paragraph: { marginBottom: 10, color: '#555', fontSize: 16 },
  list: { paddingLeft: 10 },
  footer: { marginTop: 30 },
});
