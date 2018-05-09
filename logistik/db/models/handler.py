from logistik.environ import env
from logistik.db.repr.handler import HandlerConf
from logistik.db.repr.handler import HandlerStats
from logistik.config import ModelTypes

from sqlalchemy import UniqueConstraint


class HandlerStatsEntity(env.dbman.Model):
    __tablename__ = 'handler_stats_entity'

    id = env.dbman.Column(env.dbman.Integer(), primary_key=True)
    service_id = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    name = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    event = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    endpoint = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    version = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False)
    stat_type = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False)
    event_time = env.dbman.Column(env.dbman.DateTime(), unique=False, nullable=False)
    event_id = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False)
    event_verb = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False)
    model_type = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False)
    node = env.dbman.Column(env.dbman.Integer(), unique=False, nullable=False)

    def to_repr(self) -> HandlerStats:
        return HandlerStats(
            identity=self.id,
            name=self.name,
            service_id=self.service_id,
            endpoint=self.endpoint,
            version=self.version,
            event=self.event,
            event_time=self.event_time,
            event_id=self.event_id,
            stat_type=self.stat_type,
            event_verb=self.event_verb,
            node=self.node,
            model_type=self.model_type
        )


class HandlerConfEntity(env.dbman.Model):
    id = env.dbman.Column(env.dbman.Integer(), primary_key=True)
    service_id = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    name = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    event = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    enabled = env.dbman.Column(env.dbman.Boolean(), unique=False, nullable=False)
    endpoint = env.dbman.Column(env.dbman.String(80), unique=False, nullable=False)
    version = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False, server_default='v1')
    path = env.dbman.Column(env.dbman.String(80), unique=False, nullable=True)
    node = env.dbman.Column(env.dbman.Integer(), unique=False, nullable=False, server_default='0')
    method = env.dbman.Column(env.dbman.String(10), unique=False, nullable=True)
    model_type = env.dbman.Column(env.dbman.String(16), unique=False, nullable=False, server_default=ModelTypes.MODEL)
    retries = env.dbman.Column(env.dbman.Integer(), unique=False, nullable=False, server_default='1')
    timeout = env.dbman.Column(env.dbman.Integer(), unique=False, nullable=False, server_default='0')
    tags = env.dbman.Column(env.dbman.String(128), unique=False, nullable=True)
    return_to = env.dbman.Column(env.dbman.String(80), unique=False, nullable=True)

    UniqueConstraint('service_id', 'node', 'model_type', name='uix_1')

    def to_repr(self) -> HandlerConf:
        return HandlerConf(
            identity=self.id,
            name=self.name,
            service_id=self.service_id,
            enabled=self.enabled,
            event=self.event,
            endpoint=self.endpoint,
            version=self.version,
            path=self.path,
            node=self.node,
            method=self.method,
            retries=self.retries,
            model_type=self.model_type,
            timeout=self.timeout,
            tags=self.tags,
            return_to=self.return_to
        )

    def __str__(self):
        repr_string = """
        <HandlerConfEntity 
                id={}, name={}, event={}, enabled={}, endpoint={}, 
                version={}, path={}, method={}, retries={}, timeout={}, 
                service_id={}, tags={}, return_to={}>
        """
        return repr_string.format(
            self.id, self.name, self.event, self.enabled, self.endpoint, self.version, self.path,
            self.method, self.retries, self.timeout, self.service_id, self.tags, self.return_to
        )
