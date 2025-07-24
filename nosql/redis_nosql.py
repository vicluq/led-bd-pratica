import logging
import redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nosql-redis")

# Conexão com o Redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
logger.info("Conexão estabelecida")

## Os retornos do Redis são bytes (b'value' em python), portanto precisamos converter

# String datatype
r.set('title', 'LED - Banco de Dados na Prática')

logger.info(
    f"Puxando o valor de uma chave string: {r.get('title').decode()}",
)


# Hashmaps
r.hset('user:1000', mapping={'name': 'Fulano', 'age': 30})

logger.info(
    f"Puxando todas as keys do hashmap: {r.hgetall('user:1000')}"
)

logger.info(
    f"Puxando uma Key específica do hashmap: {int(r.hget("user:1000", "age"))}",
)

logger.info(
    f"Checando se uma chave existe no hashmap: {r.hexists("user:1000", "degree")}"
)

# List
r.rpush('guideline', 'sql-vs-nosql', 'pipelines')

logger.info(
    f'Iterando uma Lista com o Redis: {[item.decode() for item in r.lrange('guideline', 0, -1)]}'
)

logger.info(
    f"""==== Listas
    Puxando elementos do final da lista: {r.rpop("guideline", 1)}
    Puxando elementos do inicio da lista: {r.lpop("guideline", 1)}
    """
)

# Sets
r.sadd('set1', 'a', 'b', 'c')
r.sadd('set2', 'b', 'c', 'd')

logger.info(
    f"""Sets
    Puxando elementos do set 1: {r.smembers('set1')}
    Puxando elementos do set 2: {r.smembers('set2')}
    """
)

logger.info(
    f"""Operações com Sets
    Unindo dois sets: {r.sunion('set1', 'set2')}
    Interseção dois sets: {r.sinter('set1', 'set2')}
    Diferença entre dois sets: {r.sdiff('set1', 'set2')}
    Descobrindo membros de um set: {r.sismember('set1', 'a') == 1}
    """
)

r.close()