from config.db import get_connection
from models.time import Time

class TimeRepository:
    def criar(self, time: Time):
        print(f"[REPOSITORY] Inserindo time: {time.nome}")
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO times (id, nome, cidade, dataFundacao, tecnico) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (time.id, time.nome, time.cidade, time.dataFundacao, time.tecnico))
        conn.commit()
        cursor.close()
        conn.close()

    def listar(self):
        print("[REPOSITORY] Buscando todos os times")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, cidade, dataFundacao, tecnico FROM times")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        print(f"[REPOSITORY] {len(rows)} time(s) encontrados")
        return [Time(*row) for row in rows]

    def atualizar(self, time: Time):
        print(f"[REPOSITORY] Atualizando time id={time.id}")
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE times SET nome=%s, cidade=%s, dataFundacao=%s, tecnico=%s WHERE id=%s"
        cursor.execute(sql, (time.nome, time.cidade, time.dataFundacao, time.tecnico, time.id))
        conn.commit()
        cursor.close()
        conn.close()

    def deletar(self, id):
        print(f"[REPOSITORY] Deletando time id={id}")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM times WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
