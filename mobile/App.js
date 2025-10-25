import React, { useState, useEffect, useRef } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, FlatList, Alert } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function App() {
  const [notes, setNotes] = useState([]);
  const [text, setText] = useState('');
  const [timerSecs, setTimerSecs] = useState(60);
  const [running, setRunning] = useState(false);
  const intervalRef = useRef(null);

  useEffect(() => {
    loadNotes();
  }, []);

  useEffect(() => {
    if (running) {
      intervalRef.current = setInterval(() => {
        setTimerSecs(s => {
          if (s <= 1) {
            clearInterval(intervalRef.current);
            setRunning(false);
            Alert.alert('Timer', 'Time is up!');
            return 0;
          }
          return s - 1;
        });
      }, 1000);
    }
    return () => clearInterval(intervalRef.current);
  }, [running]);

  async function loadNotes() {
    try {
      const raw = await AsyncStorage.getItem('notes');
      if (raw) setNotes(JSON.parse(raw));
    } catch (e) { }
  }

  async function saveNotes(newNotes){
    setNotes(newNotes);
    await AsyncStorage.setItem('notes', JSON.stringify(newNotes));
  }

  function addNote(){
    if (!text.trim()) return;
    const newNotes = [{id: Date.now().toString(), text: text.trim()}, ...notes];
    saveNotes(newNotes);
    setText('');
  }

  function removeNote(id){
    const newNotes = notes.filter(n => n.id !== id);
    saveNotes(newNotes);
  }

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Notes</Text>
      <View style={styles.row}>
        <TextInput style={styles.input} placeholder="New note" value={text} onChangeText={setText} />
        <TouchableOpacity style={styles.btn} onPress={addNote}><Text style={styles.btnText}>Add</Text></TouchableOpacity>
      </View>

      <FlatList data={notes} keyExtractor={i=>i.id} renderItem={({item})=> (
        <View style={styles.noteRow}>
          <Text style={styles.noteText}>{item.text}</Text>
          <TouchableOpacity onPress={()=>removeNote(item.id)}><Text style={styles.remove}>Del</Text></TouchableOpacity>
        </View>
      )} />

      <View style={{height:1,background:'#ddd',marginVertical:12,width:'100%'}} />

      <Text style={styles.heading}>Countdown</Text>
      <View style={styles.row}>
        <TextInput style={[styles.input,{flex:0.6}]} keyboardType="numeric" value={String(timerSecs)} onChangeText={t=>setTimerSecs(Number(t)||0)} />
        {running ? (
          <TouchableOpacity style={[styles.btn,{background:'#d9534f'}]} onPress={()=>{setRunning(false); clearInterval(intervalRef.current);}}><Text style={styles.btnText}>Stop</Text></TouchableOpacity>
        ) : (
          <TouchableOpacity style={styles.btn} onPress={()=>setRunning(true)}><Text style={styles.btnText}>Start</Text></TouchableOpacity>
        )}
      </View>
      <Text style={{fontSize:24,marginTop:8}}>{timerSecs}s</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', alignItems: 'center', paddingTop: 50, paddingHorizontal: 16 },
  heading: { fontSize: 22, fontWeight: '700', marginBottom: 8 },
  input: { borderWidth: 1, borderColor: '#ccc', padding: 8, borderRadius: 6, flex: 1, marginRight: 8 },
  btn: { backgroundColor: '#2b6cb0', paddingHorizontal: 12, paddingVertical: 10, borderRadius: 6 },
  btnText: { color: '#fff', fontWeight: '600' },
  row: { flexDirection: 'row', alignItems: 'center', width: '100%', marginBottom: 8 },
  noteRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingVertical: 8, width: '100%' },
  noteText: { flex: 1 },
  remove: { color: '#d9534f', paddingHorizontal: 8 }
});
